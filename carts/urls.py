from django.urls import path
from . import views

app_name = 'carts'


urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart_change/', views.cart_change, name='cart_change'),
]
