from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Medicine


class User(AbstractUser):
    favourites = models.ManyToManyField(Medicine, help_text='Вибрані товари', blank=True)
    cart = models.ManyToManyField(Medicine, help_text='Товари в корзині', blank=True, related_name='cart')
    photo = models.ImageField(upload_to='users_photos', help_text="Фото користувача", default='static_photos/default_profile_photo.jpg', blank=True)

    def get_fav_list(self):
        return [fav.id for fav in self.favourites.all()]
    
    def get_cart_list(self):
        return [cart.id for cart in self.cart.all()]

    class Meta:
        db_table = 'user'
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.username
