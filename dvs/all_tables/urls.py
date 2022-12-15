from django.urls import path
from .views import Page, delete_product, Prod, Add_product

urlpatterns = [
    path('providers-list/', Page, name='user-list'),
    path('', delete_product, name='delete_view'),
    path('home/', Prod.as_view(), name='products-list'),
    path('add-product/', Add_product.as_view(), name='addProduct')
]