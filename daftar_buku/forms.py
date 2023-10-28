from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Cari', max_length=100)  
