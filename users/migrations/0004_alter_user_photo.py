# Generated by Django 4.2.7 on 2024-02-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='static_photos/default_profile_photo.jpg', help_text='Фото користувача', upload_to='users_photos'),
        ),
    ]
