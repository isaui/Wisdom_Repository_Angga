from django.urls import path
from pinjam_buku.views import pinjam_buku_outer

app_name = 'pinjam_buku'

urlpatterns = [
    path('<int:id>/', pinjam_buku_outer, name='pinjam_buku'),
]