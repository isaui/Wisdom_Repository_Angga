from django.db import models
from daftar_buku.models import Rating
from authentication_bookmark.models import CustomUser

# Create your models here.
class RequestBuku(models.Model):
    isbn = models.CharField(max_length=20)
    judul = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100)
    tahun = models.IntegerField()
    kategori = models.CharField(max_length=100)
    gambar = models.CharField(max_length=100)
    deskripsi = models.TextField()
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)