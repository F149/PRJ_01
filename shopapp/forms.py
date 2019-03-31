from django import forms
from django.contrib.auth.models import User
from shopapp.models import BookShop, Book

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'first_name',
                  'last_name',
                  'email')


class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email')


class BookshopForm(forms.ModelForm):
    class Meta:
        model = BookShop
        fields = ('name',
                  'phone',
                  'address',
                  'logo')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('bookshop',)
