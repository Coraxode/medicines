from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Medicine


class User(AbstractUser):
    favourites = models.ManyToManyField(Medicine, help_text='Вибрані товари', blank=True)
    cart = models.ManyToManyField(Medicine, help_text='Товари в корзині', blank=True, related_name='cart')
    photo = models.ImageField(upload_to='users_photos', help_text="Фото користувача", default='static_photos/default_profile_photo.jpg', blank=True)

    @classmethod
    def get_user_by_username(cls, username):
        try:
            return cls.objects.get(username=username)
        except cls.DoesNotExist:
            return None

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


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Користувач', blank=True, null=True)
    medicine = models.ForeignKey(Medicine, help_text='Препарат', on_delete=models.CASCADE)
    comment = models.TextField(help_text='Коментарій', blank=True)
    date_posted = models.DateTimeField(help_text='Дата', default=timezone.now)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Коментарій'
        verbose_name_plural = 'Коментарі'

    def __str__(self):
        return f'Коментарій користувача {self.user} про препарат {self.medicine}'
