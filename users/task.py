from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import CustomUser


@shared_task
def check_active_users():
    """Функция блокировки пользователей, не заходивших более 1 месяца"""

    users = CustomUser.objects.filter(is_active=True)
    for user in users:
        if user.last_login is None:
            if user.date_joined + timedelta(days=1) < timezone.now():
                user.is_active = False
                user.save()
        elif user.last_login + timedelta(days=1) < timezone.now():
            user.is_active = False
            user.save()