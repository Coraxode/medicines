from django.shortcuts import render, redirect
from .models import Medicine, Categories


def index(request):
    return redirect('store')


def store(request):
    medicine_info = []

    for medicine in Medicine.objects.all():
        medicine_info.append({
            'name': medicine.name,
            'price': medicine.price,
            'photo': medicine.photo,
        })

    return render(request, 'store/store.html', {'medicines': medicine_info})
