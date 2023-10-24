from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Cari', max_length=100)  

class Sort(forms.Form):
    Sort = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ('judul', 'Judul'),
            ('tahun', 'Tahun'),
        )
    )