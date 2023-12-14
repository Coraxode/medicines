from django.shortcuts import render, redirect
from .models import Medicine, Categories, Forms, CountryOfOrigin


def index(request):
    return redirect('store')


def store(request):
    medicines = Medicine.objects.filter(name__icontains=request.GET.get('name', ''),
                                        price__range=(request.GET.get('minp', 0), request.GET.get('maxp', 100000)),
                                        category__in=request.GET.getlist('category', [str(i) for i in range(20)]),
                                        form__in=request.GET.getlist('form', [str(i) for i in range(20)]),
                                        country_of_origin__in=request.GET.getlist('country', [str(i) for i in range(20)]),
                                        is_prescription_required__in=request.GET.getlist('prescription', [0, 1]),
                                        )

    medicine_info = []
    for medicine in medicines:
        medicine_info.append({
            'id': medicine.id,
            'name': medicine.name,
            'price': medicine.price,
            'photo': medicine.photo,
        })

    add_info = {
        'categories': Categories.objects.values_list('id', 'name'),
        'forms': Forms.objects.values_list('id', 'name'),
        'countries': CountryOfOrigin.objects.values_list('id', 'name'),
        'min_price': Medicine.objects.order_by('price').first().price,
        'max_price': Medicine.objects.order_by('price').last().price,
        'param_list': "category, form, country, prescription",  # name, minp, maxp not included
    }

    return render(request, 'store/store.html', {'medicines': medicine_info, 'add_info': add_info})


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
