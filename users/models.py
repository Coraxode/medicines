from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Medicine


class User(AbstractUser):
    favourites = models.ManyToManyField(Medicine, help_text='Вибрані товари', blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.username
