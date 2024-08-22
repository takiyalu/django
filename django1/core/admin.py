from django.contrib import admin

# Register your models here.
from .models import Product, Cliente

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Cliente, ClientAdmin)