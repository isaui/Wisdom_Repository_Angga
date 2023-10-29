from django.contrib import admin
from pinjam_buku.models import Peminjaman, Pengembalian

# Register your models here.
admin.site.register(Peminjaman)
admin.site.register(Pengembalian)