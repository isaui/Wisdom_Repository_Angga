from django.db import models

# Create your models here.

#make model books in accordance with books.csv
class Buku(models.Model):
    isbn = models.CharField(max_length=20)
    judul = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100)
    tahun = models.IntegerField()
    kategori = models.CharField(max_length=100)
    gambar = models.CharField(max_length=100)
    deskripsi = models.TextField()
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.judul
    def __unicode__(self):
        return self.judul
    
class Rating(models.Model):
    rating = models.DecimalField(max_digits=5, decimal_places=2)



