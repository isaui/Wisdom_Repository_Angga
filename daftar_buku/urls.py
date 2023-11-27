from django.urls import path
from daftar_buku.views import show_main, make_buku, book_details, search_books, sort_books, show_xml, get_books_json, get_user, get_buku_by_author, create_request_book, get_buku_search, sort_books_json,\
sort_books_json


app_name = 'daftar_buku'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('make-book/', make_buku, name='make_book'),
    path('book_details/', book_details, name='book_details'),
    path('search/', search_books, name='search'),
    path('sort/<str:query>', sort_books, name='sort'),
    path('xml/<int:id>/', show_xml, name='show_xml'),
    path('get_books_json/', get_books_json, name='get_books_json'),
    path('get_user/', get_user, name='get_user'),
    path('get_buku_by_author/', get_buku_by_author, name='get_buku_by_author'),
    path('create-request-book/', create_request_book, name='create_request_book'),
    path('searchjson/', get_buku_search, name='get_buku_search'),
    path('sortjson/', sort_books_json, name='sort_books_json'),
]