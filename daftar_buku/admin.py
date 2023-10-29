from django.contrib import admin
from .models import Buku, Rating

# Register your models here.

@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'judul', 'penulis', 'tahun', 'kategori', 'gambar', 'deskripsi', 'rating')
    list_filter = ('kategori', 'tahun')
    search_fields = ('id', 'isbn', 'judul', 'penulis', 'tahun', 'kategori', 'gambar', 'deskripsi', 'rating')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating')
