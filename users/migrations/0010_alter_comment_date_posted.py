# Generated by Django 4.2.7 on 2024-02-09 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_comment_options_alter_comment_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Дата'),
        ),
    ]
