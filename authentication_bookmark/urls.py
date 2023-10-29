from django.urls import path
from authentication_bookmark.views import show_bookmark
from authentication_bookmark.views import register #sesuaikan dengan nama fungsi yang dibuat
from authentication_bookmark.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from authentication_bookmark.views import logout_user, delete_bookmark , add_bookmark_ajax, get_bookmark_json, show_json
from daftar_buku.views import show_main

app_name = 'authentication_bookmark'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('bookmark/', show_bookmark, name='show_bookmark'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>', delete_bookmark, name='delete_bookmark'),
    path('get-bookmark/', get_bookmark_json, name='get_bookmark_json'),
    path('add-bookmark-ajax/', add_bookmark_ajax, name='add_bookmark_ajax'),
    path('json/', show_json, name='show_json'), 
]