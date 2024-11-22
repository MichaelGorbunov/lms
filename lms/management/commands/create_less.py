from lms.models import Lesson, Course
from django.core.management.base import BaseCommand
from django.core.management import call_command
import random


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):

        for m in range(9):
            course = Course(title=f'Курс-{m + 1}', description=f'Курс-{m + 1} ' * 2)
            course.save()
            less_count=random.randint(3, 6)
            for n in range(less_count):
                lesson = Lesson(course_id =(m+1), title=f'Урок-{n + 1} курс - {m + 1} ', description=f'Урок-{n + 1} ' * 2)
                lesson.save()

