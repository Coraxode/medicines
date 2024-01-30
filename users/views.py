from django.http import JsonResponse
from django.shortcuts import render

from main.services import get_info_for_user_page, prepare_context


def login(request):
    context = {'title': 'Авторизація'}

    return render(request, 'users/login.html', context)


def signup(request):
    context = {'title': 'Реєстрація'}

    return render(request, 'users/signup.html', context)


def profile(request, username):
    user_info = get_info_for_user_page(username)
    if not user_info:
        return JsonResponse({'message': 'Not a valid username'}, status=404)
    context = prepare_context(user_info, request.user, username)

    return render(request, 'users/profile.html', context)


def logout(request):
    context = {'title': 'Вихід'}
    return render(request, '', context)
