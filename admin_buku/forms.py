from django import forms
from daftar_buku.models import Buku
from .models import RequestBuku

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

class RequestBukuForm(forms.ModelForm):
    class Meta:
        model = RequestBuku
        fields = '__all__'