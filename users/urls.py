from django.urls import path
from users import views

app_name = 'users'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    # path('user/<str:username>/', views.user_page, name='user_page'),
]
