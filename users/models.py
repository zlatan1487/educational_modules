from django.contrib.auth.models import AbstractUser
from django.db import models
from users.manager import CustomUserManager


class User(AbstractUser):
    """
        Модель пользователя с расширенными полями.
    """
    username = None

    date_of_birth = models.DateField(
        null=True, blank=True,
        verbose_name='Дата рождения')
    avatar = models.ImageField(
        upload_to='user_avatars/',
        null=True, blank=True,
        verbose_name='Аватар')
    first_name = models.CharField(
        max_length=30, blank=True,
        verbose_name='Имя')
    last_name = models.CharField(
        max_length=30, blank=True,
        verbose_name='Фамилия')
    phone = models.CharField(
        max_length=15, blank=True,
        verbose_name='Телефон')
    email = models.EmailField(
        unique=True,
        verbose_name='Почта')

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
