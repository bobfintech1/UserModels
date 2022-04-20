from django import forms
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Bro oqip ciqip toldirarsiz ')

    class Meta:
        model = Account
        fields = ['email', 'phone_number', 'password1']