from django.urls import path
from admin_buku.views import show_main, make_buku, search_books, sort_books, delete_book, request_buku, delete_request_book, get_request_books_json
from admin_buku.views import get_books_json, get_user, get_buku_by_author, book_details, create_book, edit_book, acc_request_book, request_book_details
from admin_buku.views import create_book_flutter, edit_book_flutter, delete_book_flutter, acc_request_book_flutter, delete_request_book_flutter

app_name = 'admin_buku'

urlpatterns = [
    path('', show_main, name='show_main'),

    path('request-book/', request_buku, name='request_book'),
    path('acc-request-book/<int:bookID>/', acc_request_book, name='acc_request_book'),
    path('delete-request-book/<int:bookID>/', delete_request_book, name='delete_request_book'),
    path('request_book_details/', request_book_details, name='request_book_details'),
    path('get-request-books/', get_request_books_json, name='get_request_books_json'),
    

    path('make-book/', make_buku, name='make_book'),
    path('search/', search_books, name='search'),
    path('book_details/', book_details, name='book_details'),
    path('sort/<str:query>', sort_books, name='sort'),

    path('create-book/', create_book, name='create_book'),
    path('edit-book/<int:bookID>/', edit_book, name='edit_book'),
    path('delete-book/<int:bookID>/', delete_book, name='delete_book'),
    
    path('create-book-flutter/', create_book_flutter, name='create_book_flutter'),
    path('edit-book-flutter/', edit_book_flutter, name='edit_book_flutter'),
    path('delete-book-flutter/', delete_book_flutter, name='delete_book_flutter'),
    path('acc-request-book-flutter/<int:bookID>/', acc_request_book_flutter, name='acc_request_book_flutter'),
    path('delete-request-book-flutter/<int:bookID>/', delete_request_book_flutter, name='delete_request_book_flutter'),

    path('get-books/', get_books_json, name='get_books_json'),
    path('get_user/', get_user, name='get_user'),
    path('get_buku_by_author/', get_buku_by_author, name='get_buku_by_author'),
]