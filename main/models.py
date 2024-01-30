from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'form'
        verbose_name = 'Форма випуску'
        verbose_name_plural = 'Форми випуску'

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'manufacturer'
        verbose_name = 'Виробник'
        verbose_name_plural = 'Виробники'

    def __str__(self):
        return self.name


class CountryOfOrigin(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'country'
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100, help_text="Назва препарату")
    price = models.FloatField(help_text="Ціна", default=0, blank=True)
    photo = models.TextField(help_text="Фото препарату", default='', blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, help_text="Категорія препарату (протизастудні, знеболюючі і т.д.)", blank=True, null=True)
    form = models.ForeignKey(Form, on_delete=models.DO_NOTHING, help_text="Форма випуску препарату (сироп, таблетки і т.д.)", blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING, help_text="Виробник препарату", blank=True, null=True)
    country_of_origin = models.ForeignKey(CountryOfOrigin, on_delete=models.DO_NOTHING, help_text="Країна-виробник", blank=True, null=True)
    is_prescription_required = models.BooleanField(default=False, help_text="Чи потрібен рецепт для покупки (Так/Ні)", blank=True)
    date_of_manufacture = models.DateField(help_text="Дата виготовлення", default='2001-01-01', blank=True)
    service_life = models.IntegerField(help_text="Термін придатності (в місяцях)", default=0, blank=True)
    description = models.TextField(help_text="Опис", default='', blank=True)
    quantity = models.IntegerField(help_text="Кількість препарату", default=0, blank=True)

    @classmethod
    def filter_medicines(cls, search, price_range, category, form, country, prescription, order_by):
        return cls.objects.filter(name__icontains=search,
                                  price__range=price_range,
                                  category__in=category,
                                  form__in=form,
                                  country_of_origin__in=country,
                                  is_prescription_required__in=prescription
                                  ).order_by(order_by)

    class Meta:
        db_table = 'medicine'
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препарати'

    def __str__(self):
        return f'{self.name}'
