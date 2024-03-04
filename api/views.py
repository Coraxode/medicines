from .serializers import MedicinesSerializer
from django.shortcuts import render
from rest_framework import generics
from main.models import Medicine


class MedicinesListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicinesSerializer
    queryset = Medicine.objects.all()


class MedicineRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicinesSerializer
    queryset = Medicine.objects.all()
