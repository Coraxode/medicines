# Generated by Django 4.2.7 on 2024-02-09 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_medicine_photo'),
        ('users', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='comment',
            name='medicine',
            field=models.ForeignKey(help_text='Препарат', on_delete=django.db.models.deletion.CASCADE, to='main.medicine'),
        ),
    ]
