from django import forms
from .models import AppUser, Item

class ItemCreateForm(forms.ModelForm):
    class Meta:
        fields = ("title", "particular", "lf", "price", "quantity", "total")
        model = Item

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ("full_name", "contact", "email", "password")
        model = AppUser

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ("email", "password")
        model = AppUser
