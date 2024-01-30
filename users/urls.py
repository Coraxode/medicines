from django.urls import path
from users import views

app_name = 'users'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('<str:username>/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
