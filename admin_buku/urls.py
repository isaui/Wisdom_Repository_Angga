from django.urls import path
from admin_buku.views import show_main, make_buku, search_books, sort_books, delete_book
from daftar_buku.views import show_xml, get_books_json

app_name = 'admin_buku'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('make-book/', make_buku, name='make_book'),
    path('search/', search_books, name='search'),
    path('sort/', sort_books, name='sort'),
    path('delete-book/<int:bookID>/', delete_book, name='delete_book'),
]