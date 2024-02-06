from django.urls import path
from . import views

app_name = 'carts'


urlpatterns = [
    path('cart_add/<int:medicine_id>', views.cart_add, name='cart_add'),
    path('cart_change/<int:medicine_id>', views.cart_change, name='cart_change'),
    path('cart_remove/<int:medicine_id>', views.cart_remove, name='cart_remove'),
]
