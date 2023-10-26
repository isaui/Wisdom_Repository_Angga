import datetime
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from daftar_buku.models import Buku

# Create your models here.
class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    peminjam = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_dipinjam = models.DateField(auto_now_add=True)
    tanggal_pengembalian = models.DateField(default=F("tanggal_dipinjam") + datetime.timedelta(days=3))