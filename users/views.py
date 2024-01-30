from django.http import JsonResponse
from django.shortcuts import render
from .services import get_user_by_username


def login(request):
    context = {'title': 'Авторизація'}

    return render(request, 'users/login.html', context)


def signup(request):
    context = {'title': 'Реєстрація'}

    return render(request, 'users/signup.html', context)


def profile(request, username):
    user = get_user_by_username(username)
    if not user:
        return JsonResponse({'message': 'Not a valid username'}, status=404)
    context = {
        'user_info': user,
        'title': user.username,
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    context = {'title': 'Вихід'}
    return render(request, '', context)
