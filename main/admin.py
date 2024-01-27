from django.contrib import admin
from .models import Categories, Forms, Manufacturers, CountryOfOrigin, Medicine, UserInfo


admin.site.register(Categories)
admin.site.register(Forms)
admin.site.register(Manufacturers)
admin.site.register(CountryOfOrigin)
admin.site.register(Medicine)
admin.site.register(UserInfo)
