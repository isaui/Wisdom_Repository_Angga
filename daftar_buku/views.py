from django.shortcuts import render
from daftar_buku.models import Buku
import pandas
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, Page
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.db.models.functions import Lower
from .forms import Sort
from .forms import SearchForm
from django.core import serializers
from django.http import HttpResponse

daftar_genre = [
        "Fiction",
        "Juvenile Fiction",
        "Biography & Autobiography",
        "History",
        "Literary Criticism",
        "Philosophy",
        "Comics & Graphic Novels",
        "Religion",
        "Drama",
        "Juvenile Nonfiction",
    ]


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

            return render(request, 'main.html', {'buku': buku_list,
                                                 'genre': daftar_genre,
                                                 'sort' : sortForm,})

        else:
            return render(request, 'main.html', {'form': form})
        
def sort_books(request):
   
    if request.method == 'GET':

        sort = request.GET.getlist('Sort', request.session.get('Sort'))
        buku_list = Buku.objects.all()
        if 'judul' in sort:
            buku_list = buku_list.order_by(Lower('judul'))
        if 'tahun' in sort:
            buku_list = buku_list.order_by('tahun')
        paginator = Paginator(buku_list, 12)  
        page = request.GET.get('page')
        buku = paginator.get_page(page)
        context = {
            'buku': buku,
            'genre' : daftar_genre,
            'sort' : sortForm,
        }
        request.session['Sort'] = sort
        return render(request, 'main.html', context)

  

def book_details(request):

    book_id = request.GET.get('id')
    book = Buku.objects.get(id=book_id)
    
    return JsonResponse({'judul': book.judul,
                        'penulis': book.penulis,
                        'tahun': book.tahun,
                        'kategori': book.kategori,
                        'gambar': book.gambar,
                        'deskripsi':book.deskripsi,
                        'rating': book.rating})


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

    return HttpResponseRedirect(reverse('daftar_buku:show_main'))

def show_xml(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

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
    return render(request, 'main.html', context)

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
        return render(request, 'main.html', context)
    

def get_books_json(request):
    buku_list = Buku.objects.all().order_by('rating')[:10]
    buku_list_json = serializers.serialize('json', buku_list)
    return HttpResponse(buku_list_json)



