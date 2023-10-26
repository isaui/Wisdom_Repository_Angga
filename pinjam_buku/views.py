from django.shortcuts import render
from daftar_buku.models import Buku

# Create your views here.
def pinjam_buku_outer(request, id):
    buku = Buku.objects.filter(pk=id).first()
    context = {
        'buku': buku,
    }

    return render(request, "pinjambuku.html", context)