from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    phone = models.CharField(max_length=10, verbose_name='телефон')
    avatar = models.ImageField(upload_to='users', verbose_name='аватарка', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}, {self.phone}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'