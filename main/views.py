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
    medicine = Medicine.objects.get(id=id)
    medicine_info = {
        'id': medicine.id,
        'name': medicine.name,
        'photo': medicine.photo,
        'price': medicine.price,
        'category': medicine.category.first(),
        'form': medicine.form.first(),
        'manufacturer': medicine.manufacturer.first(),
        'country_of_origin': medicine.country_of_origin.first(),
    }
    return render(request, 'store/medicine.html', {'medicine': medicine_info})
