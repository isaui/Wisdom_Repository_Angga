from django import forms
from daftar_buku.models import Buku

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'