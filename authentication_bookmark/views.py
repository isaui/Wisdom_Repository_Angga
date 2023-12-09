import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
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
    data = Buku.objects.all()    
    context = {
        'name': request.user.username,
        'member' : request.user.member,
        'bookmarks': bookmarks,
        'data' : data,
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
            if user.is_superuser:
                response = HttpResponseRedirect(reverse('admin_buku:show_main')) 
            else:
                response = HttpResponseRedirect(reverse('daftar_buku:show_main')) 
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('daftar_buku:show_main')

@csrf_exempt
def add_bookmark_ajax(request):
    if request.method == 'GET':
        id_buku = request.GET.get('id_buku')
        buku = Buku.objects.get(pk=id_buku)
        user = request.user

        # Periksa apakah buku sudah ada di bookmark user
        existing_bookmark = Bookmark.objects.filter(buku=buku, user=user)
        if existing_bookmark.exists():
            # Jika sudah ada, kirim pesan bahwa buku sudah ada di bookmark
            return JsonResponse({'message': 'Buku sudah ada di bookmark'}, status=201)

        # Jika belum ada, tambahkan ke bookmark
        new_bookmark = Bookmark(buku=buku, user=user, judul=buku.judul, gambar=buku.gambar)
        new_bookmark.save()
        return JsonResponse({'message': 'Bookmark berhasil ditambahkan'}, status=201)

    return JsonResponse({'message': 'Metode tidak diizinkan'}, status=405)
 
def get_bookmark_json(request):
    bookmark_item = Bookmark.objects.all()
    return HttpResponse(serializers.serialize('json', bookmark_item))
@csrf_exempt
def get_bookmark_user(request):
    bookmark_user = Bookmark.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", bookmark_user), content_type="application/json")

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

@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            if user.is_superuser:
                tipe = "admin"
            else:
                tipe = "biasa"
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "member": user.member,
                "tipe": tipe,
                "message": "Login sukses!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def logout_flutter(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)

@csrf_exempt
def register_flutter(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                "message": "Registrasi berhasil!"
            }, status=200)
        else:
            errors = form.errors.get_json_data(escape_html=False)  # Mendapatkan pesan kesalahan form
            return JsonResponse({
                "status": False,
                "errors": errors,
                "message": "Registrasi gagal, silakan perbaiki data yang dimasukkan."
            }, status=400)
    else:
        return JsonResponse({
            "status": False,
            "message": "Registrasi gagal, metode request tidak valid."
        }, status=405)


