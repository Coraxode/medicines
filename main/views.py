from django.shortcuts import render, redirect
from .models import Medicine, Categories


def index(request):
    return redirect('store')


def store(request):
    medicines = Medicine.objects.filter(name__icontains=request.GET.get('name', ''),
                                        price__range=(request.GET.get('minp', 0), request.GET.get('maxp', 100000)),
                                        category__in=request.GET.get('category', ','.join([str(i) for i in range(20)])).split(','),
                                        form__in=request.GET.get('form', ','.join([str(i) for i in range(20)])).split(','),
                                        country_of_origin__in=request.GET.get('country', ','.join([str(i) for i in range(20)])).split(','),
                                        is_prescription_required__in=request.GET.get('prescription', '0,1').split(','),
                                        )

    medicine_info = []
    for medicine in medicines:
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
