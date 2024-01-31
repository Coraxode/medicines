from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={"autofocus": True,
#                                       'placeholder': 'Введіть email',
#                                       })
#         )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
#                                           'placeholder': 'Введіть пароль',
#                                           }),
#         )

#     class Meta:
#         model = User
#         fields = ['username', 'password']
