from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    """Пользовательская модель пользователя, расширяющая AbstractUser."""

    username = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "A user with that email already exists.",
        },
    )

    # Базовые поля
    first_name = models.CharField(max_length=30, blank=True) # имя
    last_name = models.CharField(max_length=30, blank=True) # фамилия
    is_moderator = models.BooleanField(default=False) # флаг, указывающий, является ли пользователь модератором

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
