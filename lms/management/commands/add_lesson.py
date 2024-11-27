import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from lms.models import Course, Lesson


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        call_command(
            "loaddata", os.path.join(settings.BASE_DIR, "data", "course_fixture.json")
        )
        call_command(
            "loaddata", os.path.join(settings.BASE_DIR, "data", "lesson_fixture.json")
        )
