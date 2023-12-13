from django.shortcuts import render, redirect
from .models import Medicine, Categories


def index(request):
    return redirect('store')


def store(request):
    medicine_info = []

    for medicine in Medicine.objects.all():
        medicine_info.append({
            'id': medicine.id,
            'name': medicine.name,
            'price': medicine.price,
            'photo': medicine.photo,
        })

    return render(request, 'store/store.html', {'medicines': medicine_info})


def medicine_page(request, id):
    return render(request, 'store/medicine.html')
