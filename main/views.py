from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services import search_medicines, get_info_for_filters, \
    check_authenticated, get_info_for_user_page, add_to_favourites


def index(request):
    return redirect('store')


def store(request):
    if request.method == 'POST':
        add_to_favourites(request.POST['username'], request.POST['medicine_id'])
        return redirect(request.path)

    medicines = search_medicines(request)
    medicines['filters'] = get_info_for_filters(medicines['medicines'])
    context = check_authenticated(medicines, request.user)

    return render(request, 'store/store.html', context)


def medicine_page(request, id):
    medicine = search_medicines(search_by_id=id)
    if not medicine['medicine']:
        return JsonResponse({'message': 'Not a valid ID'}, status=404)
    context = check_authenticated(medicine, request.user)

    return render(request, 'store/medicine.html', context)


def user_page(request, username):
    if request.method == 'POST':
        add_to_favourites(request.POST['username'], request.POST['medicine_id'])
        return redirect(request.path)

    user_info = get_info_for_user_page(username)
    if not user_info:
        return JsonResponse({'message': 'Not a valid username'}, status=404)
    context = check_authenticated(user_info, request.user)

    return render(request, 'store/user_page.html', context)
