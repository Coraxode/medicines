from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('medicines/', views.MedicinesListCreateView.as_view(), name='index'),
    path('medicine/<int:pk>/', views.MedicineRetrieveView.as_view(), name='medicine_detail'),
]
