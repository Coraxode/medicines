from django.shortcuts import render
from .models import Medicine, Categories


def index(request):
    medicine_info = []

    for medicine in Medicine.objects.all():
        print(medicine.category.first())
        medicine_info.append({
            'id': medicine.id,
            'name': medicine.name,
            'price': medicine.price,
            'photo': medicine.photo,
            'is_prescription_required': medicine.is_prescription_required,
            'date_of_manufacture': medicine.date_of_manufacture,
            'service_life': medicine.service_life,
            'description': medicine.description,
            'quantity': medicine.quantity,
            'category': medicine.category.first(),
            'form': medicine.form.first(),
            'manufacturer': medicine.manufacturer.first(),
            'country_of_origin': medicine.country_of_origin.first(),
        })

    return render(request, 'store/store.html', {'medicines': medicine_info})
