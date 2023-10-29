import datetime
from django.db import models
from django.db.models import F
from authentication_bookmark.models import CustomUser
from daftar_buku.models import Buku

# Create your models here.
class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    peminjam = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    idBuku = models.IntegerField()
    tanggal_dipinjam = models.DateField(auto_now_add=True)
    hari = models.IntegerField(null=True, blank=True)
    tanggal_pengembalian = models.DateField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.tanggal_dipinjam = datetime.datetime.now().date()
        if not self.hari:
            if self.peminjam.member.lower() == "premium":
                self.hari = 7
            else:
                self.hari = 3
        if not self.tanggal_pengembalian:
            self.tanggal_pengembalian = self.tanggal_dipinjam + datetime.timedelta(days=self.hari)
        super(Peminjaman, self).save(*args, **kwargs)

class Pengembalian(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    peminjam = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    idBuku = models.IntegerField()
    review = models.BooleanField(default=False)