from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Main.models import Categorie, Order, Poid, Produit, Region, SousCategorie, Vendeur, Ville, AfterCat

# Register your models here.
# from Main.models import


# class UserModel(UserAdmin):
#     ordering = ('username',)
admin.site.site_header = "Louma Administrateur"
admin.site.index_title = "Bienvenue dans l'administration de Louma"
admin.site.site_title = "Louma Admin"


# admin.site.register(UserAdmin)
admin.site.register(Categorie)
admin.site.register(AfterCat)
admin.site.register(SousCategorie)
admin.site.register(Produit)
admin.site.register(Poid)
admin.site.register(Vendeur)
admin.site.register(Region)
admin.site.register(Ville)
admin.site.register(Order)
