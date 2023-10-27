from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class SignupForm(UserCreationForm):
    member = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[
            ('regular', 'Regular'),
            ('premium', 'Premium')
        ],
        initial='regular'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'member')
