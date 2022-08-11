from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# from django.urls import reverse
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ville(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, null=False, default="")

    def __str__(self):
        return self.name


class Vendeur(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    nom_boutique = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class AfterCat(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SousCategorie(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    aftercat = models.ForeignKey(
        AfterCat, on_delete=models.CASCADE, null=False, default="")
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Poid(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Produit(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    image2 = models.ImageField(null=False, default="")
    image3 = models.ImageField(null=False, default="")
    price = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    reduction = models.IntegerField(null=False, default=0)
    price_before = models.IntegerField(null=False, default=0)
    quantity = models.IntegerField(null=False, default=0)
    poid = models.ForeignKey(
        Poid, on_delete=models.CASCADE, null=False, default="")

    desc1 = models.CharField(max_length=255, null=False, default="")
    desc2 = models.CharField(max_length=255, null=False, default="")
    desc3 = models.CharField(max_length=255, null=False, default="")
    desc4 = models.CharField(max_length=255, null=False, default="")
    fulldesc = models.TextField(null=False, default="")
    id_vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    souscategory = models.ForeignKey(SousCategorie, on_delete=models.CASCADE)
    aftercat = models.ForeignKey(
        AfterCat, on_delete=models.CASCADE, null=False, default="")

    def __str__(self):
        return self.name


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={
                             'exixts': 'Cette email existe deja'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = "Entrez votre nom d'utilisateur"
        self.fields['email'].widget.attrs['placeholder'] = "Entrez votre nom email"
        self.fields['password1'].widget.attrs['placeholder'] = "Entrez votre mot de passe"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirmé mot de passe"

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(
                self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    age = models.IntegerField()
    sexe = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    country = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    total = models.FloatField()
    payment_mode = models.CharField(max_length=255, null=False, default="")
    payment_id = models.CharField(max_length=255, null=False, default="")
    orderstatuses = (
        ('En attente', 'En attente'),
        ('Pour expedition', 'Pour expedition'),
        ('Complete', 'Complete'),
    )
    status = models.CharField(
        max_length=255, choices=orderstatuses, null=False, default="En attente")
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=255, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=False, default="")
    produit = models.ForeignKey(
        Produit, on_delete=models.CASCADE, null=False, default="")
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)
