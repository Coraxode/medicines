from django.shortcuts import redirect, render
from carts.services import add_to_cart


def cart(request):
    context = {
        'title': 'Корзина',
    }
    
    return render(request, 'carts/cart.html', context)


def cart_change(request):
    if request.POST:
        add_to_cart(request.POST.get('username'), request.POST.get('medicine_id'))
        return redirect(request.POST.get('url'))
