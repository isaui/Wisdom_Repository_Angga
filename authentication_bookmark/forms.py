from django.forms import ModelForm
from authentication_bookmark.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]