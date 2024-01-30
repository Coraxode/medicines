from django.urls import path
from . import views

app_name = 'store'


urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('medicine/<int:id>/', views.medicine_page, name='medicine_page'),
]
