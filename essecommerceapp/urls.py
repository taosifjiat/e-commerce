from django.urls import path
from .views import *
urlpatterns = [
    path('', all_product),
    path('cart',cart),
    path('checkout',checkout),
    path('updateitem',updateItem,name='updateitem'),
]
