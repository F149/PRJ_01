"""prj_bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopapp import views

from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('shopapp/sign-in/', auth_views.LoginView.as_view(), name="shopapp-sign-in"),
    path('shopapp/sign-out/', auth_views.LogoutView.as_view(), name="shopapp-sign-out"),

    path('shopapp/', views.shopapp_home, name='shopapp-home'),

    path('shopapp/sign-up/', views.shopapp_sign_up, name='shopapp-sign-up'),
    path('shopapp/account/', views.shopapp_account, name='shopapp-account'),
    path('shopapp/book/', views.shopapp_book, name='shopapp-book'),
    path('shopapp/book/add/', views.shopapp_add_book, name='shopapp-add-book'),
    path('shopapp/book/edit/<int:book_id>/', views.shopapp_edit_book, name='shopapp-edit-book')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
