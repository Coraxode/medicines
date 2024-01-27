from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('medicine/<int:id>/', views.medicine_page, name='medicine_page'),
    path('user/<str:username>/', views.user_page, name='user_page'),
]
