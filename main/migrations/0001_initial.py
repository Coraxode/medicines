# Generated by Django 4.2.7 on 2024-01-30 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CountryOfOrigin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'form',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Назва препарату', max_length=100)),
                ('price', models.FloatField(blank=True, default=0, help_text='Ціна')),
                ('photo', models.TextField(blank=True, default='', help_text='Фото препарату')),
                ('is_prescription_required', models.BooleanField(blank=True, default=False, help_text='Чи потрібен рецепт для покупки (Так/Ні)')),
                ('date_of_manufacture', models.DateField(blank=True, default='2001-01-01', help_text='Дата виготовлення')),
                ('service_life', models.IntegerField(blank=True, default=0, help_text='Термін придатності (в місяцях)')),
                ('description', models.TextField(blank=True, default='', help_text='Опис')),
                ('quantity', models.IntegerField(blank=True, default=0, help_text='Кількість препарату')),
                ('category', models.ForeignKey(blank=True, help_text='Категорія препарату (протизастудні, знеболюючі і т.д.)', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.category')),
                ('country_of_origin', models.ForeignKey(blank=True, help_text='Країна-виробник', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.countryoforigin')),
                ('form', models.ForeignKey(blank=True, help_text='Форма випуску препарату (сироп, таблетки і т.д.)', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.form')),
                ('manufacturer', models.ForeignKey(blank=True, help_text='Виробник препарату', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.manufacturer')),
            ],
            options={
                'verbose_name': 'Препарат',
                'verbose_name_plural': 'Препарати',
                'db_table': 'medicine',
            },
        ),
    ]
