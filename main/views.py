from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services import search_medicines, get_info_for_filters, \
    prepare_context, add_to_favourites


def index(request):
    return redirect('store')


def store(request):
    if request.method == 'POST':
        add_to_favourites(request.POST['username'], request.POST['medicine_id'])
        return redirect(request.POST['url'])

    medicines = search_medicines(request)
    medicines['filters'] = get_info_for_filters(medicines['medicines'])
    context = prepare_context(medicines, request.user, 'Medicines')

    return render(request, 'store/store.html', context)


def medicine_page(request, id):
    medicine = search_medicines(search_by_id=id)
    if not medicine['medicine']:
        return JsonResponse({'message': 'Not a valid ID'}, status=404)
    context = prepare_context(medicine, request.user, medicine['medicine'].name)

    return render(request, 'store/medicine.html', context)
