from django.shortcuts import render
from daftar_buku.models import Buku
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, Page
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.db.models.functions import Lower
from daftar_buku.forms import Sort, SearchForm
from daftar_buku.views import daftar_genre
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
import pandas

@require_http_methods(["DELETE"])
def delete_book(request, bookID):
    book = Buku.objects.get(pk=bookID)

    if request.method == 'DELETE':
        book.delete()
        return JsonResponse({'success': True,})

def search_books(request):
    if not request.method == 'POST':
        if 'search-books' in request.session:
            if 'search-books' in request.session:
                request.POST = request.session['search-books']
            request.method = 'POST'

    if request.method == 'POST':
        form = SearchForm(request.POST)
        request.session['search-books'] = request.POST

        if form.is_valid():
            query = form.cleaned_data['query']
            buku_list = Buku.objects.filter(Q(judul__icontains=query) | Q(penulis__icontains=query) | Q(kategori__icontains=query))

            paginator = Paginator(buku_list, 12)
            page = request.GET.get('page', 1)

            try:
                buku_list = paginator.page(page)
            except PageNotAnInteger:
                buku_list = paginator.page(1)
            except EmptyPage:
                buku_list = paginator.page(paginator.num_pages)

            return render(request, 'main-admin.html', {'buku': buku_list,
                                                 'genre': daftar_genre,
                                                 'sort' : sortForm,})

        else:
            return render(request, 'main-admin.html', {'form': form})
        
def sort_books(request):
   
    if request.method == 'GET':

        sort = request.GET.getlist('Sort', request.session.get('Sort'))
        buku_list = Buku.objects.all()
        if 'judul' in sort:
            buku_list = buku_list.order_by(Lower('judul'))
        if 'tahun' in sort:
            buku_list = buku_list.order_by('tahun')
        if 'rating' in sort:
            buku_list = buku_list.order_by('-rating')
        paginator = Paginator(buku_list, 12)  
        page = request.GET.get('page')
        buku = paginator.get_page(page)
        context = {
            'buku': buku,
            'genre' : daftar_genre,
            'sort' : sortForm,
        }
        request.session['Sort'] = sort
        return render(request, 'main-admin.html', context)

def make_buku(request):

    file_csv = open('daftar_buku\\static\\books.csv', 'r', encoding='utf-8')
    data = pandas.read_csv(file_csv, encoding='utf-8')

    buku = {}
    buku['isbn'] = data['isbn13'].tolist()
    buku['judul'] = data['title'].tolist()
    buku['penulis'] = data['authors'].tolist()
    buku['tahun'] = data['published_year'].tolist()
    buku['kategori'] = data['categories'].tolist()
    buku['gambar'] = data['thumbnail'].tolist()
    buku['deskripsi'] = data['description'].tolist()
    buku['rating'] = data['average_rating'].tolist()

    counter = 0
    for i in range(0, len(data['isbn13'])):
        try:
            if counter == 100:
                break
            buku_obj = Buku(isbn=buku['isbn'][i], judul=buku['judul'][i], penulis=buku['penulis'][i], tahun=buku['tahun'][i], kategori=buku['kategori'][i], gambar=buku['gambar'][i], deskripsi=buku['deskripsi'][i], rating=buku['rating'][i])
            buku_obj.save()
            counter += 1
        except:
            print("tesss")
            pass

    return HttpResponseRedirect(reverse('admin_buku:show_main'))

sortForm = Sort()

def show_main(request):

    if(len(Buku.objects.all()) == 0):
        make_buku(request)    
    buku_list = Buku.objects.all()
    paginator = Paginator(buku_list, 12)  
    page = request.GET.get('page')
    buku = paginator.get_page(page)
    context = {
        'buku': buku,
        'sort' : sortForm,
        'genre' : daftar_genre
    }
    return render(request, 'main-admin.html', context)

def sort(request):
    if request.method == 'GET':
        sort = request.GET.get('sort')
        if sort == 'judul':
            buku_list = Buku.objects.all().order_by(Lower('judul'))
        elif sort == 'tahun':
            buku_list = Buku.objects.all().order_by('tahun')
        else:
            buku_list = Buku.objects.all()
        paginator = Paginator(buku_list, 12)  
        page = request.GET.get('page')
        buku = paginator.get_page(page)
        context = {
            'buku': buku,
            'genre': daftar_genre,
            'sort' : sortForm,
        }
        return render(request, 'main-admin.html', context)