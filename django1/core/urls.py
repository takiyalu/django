from django.urls import path
from .views import index, contact, product

### We create this separate url file in order to make sure that every application takes care of their own urls and not
### concentrate everything in the project urls.

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('product/<int:pk>', product, name='product'),
]

