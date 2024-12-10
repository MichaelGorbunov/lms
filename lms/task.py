from datetime import datetime, timedelta
from django.utils import timezone

from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404


from config import settings
from lms.models import Course, Subscription
from users.models import CustomUser


@shared_task
def send_email_to_subs_after_updating_course(course_pk):
    """Функция отправки сообщения об обновлении курса подписчикам."""
    course = get_object_or_404(Course, pk=course_pk)
    subs = Subscription.objects.filter(course=course.pk)
    if subs:
        print("Рассылка запущена")
        send_mail(
            subject=f"Обновление курса {course.title}",
            message=f"Здравствуйте! Курс {course.title} обновлен! Скорее посмотрите, что изменилось!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.user.email for sub in subs],
        )
        print("Рассылка завершена")

@shared_task
def my_task():
    time = datetime.now()

    print(f"time now: {time}")

@shared_task
def check_active_users():
    """Функция блокировки пользователей, не заходивших более 1 месяца"""

    users = CustomUser.objects.filter(is_active=True)
    for user in users:
        if user.last_login is None:
            if user.date_joined + timedelta(days=30) < timezone.now():
                user.is_active = False
                user.save()
        elif user.last_login + timedelta(days=30) < timezone.now():
            user.is_active = False
            user.save()