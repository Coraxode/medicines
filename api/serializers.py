from rest_framework import serializers
from main.models import Medicine


class MedicinesSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    form = serializers.CharField(source='form.name')
    manufacturer = serializers.CharField(source='manufacturer.name')
    country_of_origin = serializers.CharField(source='country_of_origin.name')
    
    class Meta:
        model = Medicine
        fields = ['id',
                  'name',
                  'price',
                  'category',
                  'form',
                  'manufacturer',
                  'country_of_origin',
                  'is_prescription_required',
                  'date_of_manufacture',
                  'service_life',
                  'quantity']
