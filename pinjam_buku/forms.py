from django.forms import ModelForm
from pinjam_buku.models import Peminjaman

class PeminjamanForm(ModelForm):
    class Meta:
        model = Peminjaman
        fields = ["idBuku"]