from django.db import models
from django.contrib.auth.models import AbstractUser



NULLABLE = {"blank": True, "null": True}

class CustomUser(AbstractUser):


    first_name = models.CharField(
        max_length=50, verbose_name="имя", help_text="Укажите имя", **NULLABLE
    )
    last_name = models.CharField(
        max_length=50, verbose_name="фамилия", help_text="Укажите фамилию", **NULLABLE
    )
    email = models.EmailField(
        unique=True, verbose_name="email", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=10,
        verbose_name="телефон",
        help_text="Укажите номер телефона",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="аватар",
        help_text="Загрузите аватар",
        default="users/avatars/default.jpg",
        **NULLABLE
    )
    city = models.CharField(
        max_length=50, verbose_name="город", help_text="Укажите Ваш город", **NULLABLE
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email

# Create your models here.
