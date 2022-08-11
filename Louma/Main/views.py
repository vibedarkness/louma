from ast import While
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from Main.models import Order, UserCreateForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from Main.models import Categorie, Produit
import random


# Create your views here.
def Master(request):
    return render(request, 'master.html')


def index(request):
    categorie = Categorie.objects.all()
    produit = Produit.objects.all()
    categorieId = request.GET.get('categorie')
    if categorieId:
        produit = Produit.objects.filter(
            aftercat=categorieId).order_by('-id')
    else:
        produit = Produit.objects.all()

    context = {
        'categorie': categorie,
        'produit': produit
    }

    return render(request, 'index.html', context)


# def checkoutindex(request):

#     return render(request, 'checkout.html')


# def cartindex(request):
#     categorie = Categorie.objects.all()

#     context = {
#         'categorie': categorie,

#     }
#     return render(request, 'cart.html', context)


# def product_detail(request):
#     return render(request, 'details_produit.html')


# def login(request):
#     return render(request, 'login.html')


def Master(request):
    return render(request, 'master.html')


# def register(request):
#     categorie = Categorie.objects.all()
#     produit = Produit.objects.all()
#     categorieId = request.GET.get('categorie')
#     if categorieId:
#         produit = Produit.objects.filter(
#             aftercat=categorieId).order_by('-id')
#     else:
#         produit = Produit.objects.all()

#     context = {
#         'categorie': categorie,
#         'produit': produit
#     }

#     return render(request, 'register.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],



            )
            login(request, new_user)
            return redirect('/')
    else:
        form = UserCreateForm()
        context = {
            'form': form,
        }

    return render(request, 'registration/register.html', context)


@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Produit.objects.get(id=id)
    cart.add(product=product)
    return HttpResponseRedirect("/")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Produit.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Produit.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Produit.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart_details.html')


def checkout(request):
    return render(request, 'checkout.html')


@login_required()
def placeorder(request):
    if request.method == "POST":
        neworder = Order()
        neworder.user = request.user
        neworder.first_name = request.POST.get('prenom')
        neworder.last_name = request.POST.get('nom')
        neworder.address = request.POST.get('adresse')
        neworder.sexe = request.POST.get('sexe')
        neworder.age = request.POST.get('age')
        neworder.phone = request.POST.get('phone')

        neworder.payment_mode = request.POST.get('payment_mode')

        cart = request.session.get('cart')
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.price * item.quantity
        neworder.total = cart_total_price

        trackno = 'Louma'+str(random.Randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'Louma'+str(random.Randint(1111111, 9999999))

        neworder.tracking_no = trackno

        neworder.save()

    return redirect("/")


def product_detail(request):
    return render(request, 'details_produit.html')
