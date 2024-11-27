import random

from django.core.management.base import BaseCommand

from lms.models import Course, Lesson


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):

        for m in range(9):
            course = Course(
                title=f"Курс-{m + 1}",
                description=f"Курс-{m + 1} " * 2,
                owner_id=random.randint(1, 5),
            )
            course.save()
            less_count = random.randint(3, 6)
            for n in range(less_count):
                lesson = Lesson(
                    course_id=(m + 1),
                    title=f"Урок-{n + 1} курс - {m + 1} ",
                    description=f"Урок-{n + 1} " * 2,
                    owner_id=random.randint(1, 5),
                )
                lesson.save()
