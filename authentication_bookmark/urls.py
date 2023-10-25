from django.urls import path
from authentication_bookmark.views import show_main
from authentication_bookmark.views import register #sesuaikan dengan nama fungsi yang dibuat
from authentication_bookmark.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from authentication_bookmark.views import logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]