from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm
from .services import get_user_by_username


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('store:store'))
    else:
        form = UserLoginForm()

    context = {'title': 'Авторизація',
               'form': form,
               }

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
