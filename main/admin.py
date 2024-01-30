from django.contrib import admin
from .models import Category, Form, Manufacturer, CountryOfOrigin, Medicine


admin.site.register(Category)
admin.site.register(Form)
admin.site.register(Manufacturer)
admin.site.register(CountryOfOrigin)
admin.site.register(Medicine)
