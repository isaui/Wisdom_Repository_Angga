from django.urls import path
from daftar_buku.views import show_main, make_buku, book_details, search_books, sort_books, show_xml, get_books_json


app_name = 'daftar_buku'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('make-book/', make_buku, name='make_book'),
    path('book_details/', book_details, name='book_details'),
    path('search/', search_books, name='search'),
    path('sort/', sort_books, name='sort'),
    path('xml/<int:id>/', show_xml, name='show_xml'),
    path('get_books_json/', get_books_json, name='get_books_json'),
]