import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import datetime
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.views.decorators.csrf import csrf_exempt
from authentication_bookmark.models import Bookmark
from django.core import serializers
from daftar_buku.models import Buku

# Create your views here.
@login_required(login_url='/login')
def show_bookmark(request):
    bookmarks = Bookmark.objects.filter(user=request.user)    
    context = {
        'name': request.user.username,
        'member' : request.user.member,
        'bookmarks': bookmarks,
    }

    return render(request, "bookmark.html", context)

def register(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication_bookmark:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('daftar_buku:show_main')) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('authentication_bookmark:login')

@csrf_exempt
def add_bookmark_ajax(request):
    if request.method == 'GET':
        id_buku = request.GET.get('id_buku')
        buku = Buku.objects.get(pk=id_buku)
        user = request.user

        new_bookmark = Bookmark(buku=buku, user=user)
        new_bookmark.save()
        return JsonResponse({'message': 'Bookmark berhasil ditambahkan'}, status=201)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_buku = data.get('idbuku')  # Pastikan kunci dalam data adalah 'idbuku'
            buku = Buku.objects.get(pk=id_buku)
            user = request.user

            new_bookmark = Bookmark(buku=buku, user=user)
            new_bookmark.save()

            return JsonResponse({'message': 'Bookmark berhasil ditambahkan'}, status=201)
        except Buku.DoesNotExist:
            return JsonResponse({'message': 'ID buku tidak ditemukan'}, status=400)
        except Exception as e:
            return JsonResponse({'message': f'Gagal menambahkan bookmark: {str(e)}'}, status=400)

    return JsonResponse({'message': 'Metode tidak diizinkan'}, status=405)

# def add_bookmark_ajax(request, id):
#     # Get data berdasarkan ID
#     buku = Buku.objects.get(pk = id)
#     user = request.user
#     # Hapus data
#     new_bookmark = Bookmark(buku=buku, user=user)
#     new_bookmark.save()

#     return HttpResponse(b"CREATED", status=201)
  
 
def get_bookmark_json(request):
    bookmark_item = Bookmark.objects.all()
    return HttpResponse(serializers.serialize('json', bookmark_item))

def show_json(request):
    data = Bookmark.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_bookmark(request, id):
    # Get data berdasarkan ID
    buku = Bookmark.objects.get(pk = id)
    # Hapus data
    buku.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('authentication_bookmark:show_bookmark'))