from django.urls import path
from pinjam_buku.views import pinjam_buku_outer, lihatbukudipinjam, get_peminjaman_json, get_peminjaman_json_by_id, pengembalian_by_ajax, show_pengembalian

app_name = 'pinjam_buku'

urlpatterns = [
    path('details/<int:id>/', pinjam_buku_outer, name='pinjam_buku'),
    path('borrowed/', lihatbukudipinjam, name="list_pinjam"),
    path('peminjamanjson/', get_peminjaman_json, name="get_peminjaman_json"),
    path('peminjamanjsonbyid/<int:id>', get_peminjaman_json_by_id, name="get_peminjaman_json_by_id"),
    path('pengembalianbyajax', pengembalian_by_ajax, name="pengembalian_ajax"),
    path('returned/', show_pengembalian, name="show_pengembalian"),
]