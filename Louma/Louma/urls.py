"""Louma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from Louma import settings
from Main import views

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master', views.Master),
    path('', views.index),
    # path('checkout', views.checkoutindex),
    # path('cart', views.cartindex),
    path('register', views.register),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('product_detail', views.product_detail),

    # Ajout cart
    path('cart/<int:id>/item_increment/',
         views.item_increment, name='item_increment'),
    path('cart/<int:id>/item_decrement/',
         views.item_decrement, name='item_decrement'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/', views.cart_detail, name='cart_detail'),

    path('checkout/', views.checkout, name='checkout'),
    path('placeorder/', views.placeorder, name='placeorder'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
