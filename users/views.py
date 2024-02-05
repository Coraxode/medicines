from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserProfileForm, UserSignupForm
from .services import get_user_by_username
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('store:store'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизація',
        'form': form,
    }

    return render(request, 'users/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('store:store'))
    else:
        form = UserSignupForm()
    
    context = {
        'title': 'Реєстрація',
        'form': form,
    }

    return render(request, 'users/signup.html', context)


@login_required
def profile(request, username):
    user = get_user_by_username(username)
    if not user:
        return JsonResponse({'message': 'Not a valid username'}, status=404)

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile', kwargs={'username': user.username}))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'user_info': user,
        'title': user.username,
        'form': form,
    }

    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('store:store'))
