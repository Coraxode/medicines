from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Forms(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manufacturers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CountryOfOrigin(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100, help_text="Назва препарату")
    price = models.FloatField(help_text="Ціна", default=0, blank=True)
    photo = models.TextField(help_text="Фото препарату", default='', blank=True)
    category = models.ManyToManyField(Categories, help_text="Категорія препарату (протизастудні, знеболюючі і т.д.)", blank=True)
    form = models.ManyToManyField(Forms, help_text="Форма випуску препарату (сироп, таблетки і т.д.)", blank=True)
    manufacturer = models.ManyToManyField(Manufacturers, help_text="Виробник препарату", blank=True)
    country_of_origin = models.ManyToManyField(CountryOfOrigin, help_text="Країна-виробник", blank=True)
    is_prescription_required = models.BooleanField(default=False, help_text="Чи потрібен рецепт для покупки (Так/Ні)", blank=True)
    date_of_manufacture = models.DateField(help_text="Дата виготовлення", blank=True)
    service_life = models.IntegerField(help_text="Термін придатності (в місяцях)", blank=True)
    description = models.TextField(help_text="Опис", blank=True)
    quantity = models.IntegerField(help_text="Кількість препарату", default=0, blank=True)

    @classmethod
    def filter_medicines(cls, search, price_range, category, form, country, prescription):
        return cls.objects.filter(name__icontains=search,
                                  price__range=price_range,
                                  category__in=category,
                                  form__in=form,
                                  country_of_origin__in=country,
                                  is_prescription_required__in=prescription)

    def __str__(self):
        return f'{self.name}'


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    favourites = models.ManyToManyField(Medicine, help_text='Вибрані товари', blank=True)

    def __str__(self):
        return f'{self.user} info'
