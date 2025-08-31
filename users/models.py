from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ("user", "User"),
        ("admin", "Admin"),
    )

    username = None
    first_name = models.CharField(max_length=30, help_text="Укажите ваше имя")
    last_name = models.CharField(max_length=30, help_text="Укажите вашу фамилию")
    phone = models.CharField(
        max_length=15, blank=True, null=True, help_text="Укажите ваш номер телефона"
    )
    email = models.EmailField(unique=True, help_text="Укажите вашу почту")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")
    image = models.ImageField(
        upload_to="photo/avatar",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    token = models.CharField(
        max_length=100, verbose_name="Токен пользователя", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
