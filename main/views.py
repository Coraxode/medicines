from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services import search_medicines, get_info_for_filters
from users.services import add_to_favourites


def index(request):
    return redirect('store:store')


def store(request):
    if request.POST:
        add_to_favourites(request.POST.get('username'), request.POST.get('medicine_id'))
        return redirect(request.POST.get('url'))

    medicines = search_medicines(request)
    medicines['filters'] = get_info_for_filters(medicines['medicines'])
    context = medicines
    context['title'] = 'Головна'

    return render(request, 'store/store.html', context)


def medicine_page(request, id):
    medicine = search_medicines(search_by_id=id)
    if not medicine['medicine']:
        return JsonResponse({'message': 'Not a valid ID'}, status=404)
    context = medicine
    context['title'] = medicine['medicine'].name

    return render(request, 'store/medicine.html', context)
