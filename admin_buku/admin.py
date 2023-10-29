from django.contrib import admin
from .models import RequestBuku

# Register your models here.

@admin.register(RequestBuku)
class RequestBukuAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'judul', 'penulis', 'tahun', 'kategori', 'gambar', 'deskripsi', 'rating', 'user')
    list_filter = ('kategori', 'tahun')
    search_fields = ('id', 'isbn', 'judul', 'penulis', 'tahun', 'kategori', 'gambar', 'deskripsi', 'rating')
