# Generated by Django 4.2.7 on 2024-02-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_favourites_user_favourites'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Користувач', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='', help_text='Фото користувача', upload_to='users_photos'),
        ),
    ]