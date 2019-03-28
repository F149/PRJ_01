from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from shopapp.forms import UserForm, BookshopForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return redirect(shopapp_home)


@login_required(login_url='/shopapp/sign-in/')
def shopapp_home(request):
    return render(request, 'shopapp/home.html', {})

@login_required(login_url='/shopapp/sign-account/')
def shopapp_account(request):
    return render(request, 'shopapp/account.html', {})

@login_required(login_url='/shopapp/book/')
def shopapp_book(request):
    return render(request, 'shopapp/book.html', {})


def shopapp_sign_up(request):
    user_form = UserForm()
    book_shop_form = BookshopForm()

    if request.method == 'POST':
        user_form =  UserForm(request.POST)
        book_shop_form = BookshopForm(request.POST, request.FILES)

        if user_form.is_valid() and book_shop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_book_shop = book_shop_form.save(commit=False)
            new_book_shop.owner = new_user
            new_book_shop.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password'],
            ))

            return redirect(shopapp_home)

    return render(request, 'shopapp/sign_up.html', {
        'user_form': user_form,
        'book_shop_form': book_shop_form,
    })
