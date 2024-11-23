from lms.models import Lesson, Course
from unidecode import unidecode
from users.models import CustomUser
from django.core.management.base import BaseCommand
from django.core.management import call_command
import random


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):

        # for m in range(9):
        #     course = Course(title=f'Курс-{m + 1}', description=f'Курс-{m + 1} ' * 2)
        #     course.save()
        #     less_count=random.randint(3, 6)
        #     for n in range(less_count):
        #         lesson = Lesson(course_id =(m+1), title=f'Урок-{n + 1} курс - {m + 1} ', description=f'Урок-{n + 1} ' * 2)
        #         lesson.save()
        fname=["Петр","Иван","Сергей","Антон"]
        lname=["Иванов","Петров","Сергеев","Васин","Антонов"]
        for m in range(19):
            first_nm = random.choice(fname)
            last_nm = random.choice(lname)
            email_str = str(m + 1) + unidecode(first_nm + last_nm) + "@lms.ru"

            user=CustomUser(first_name=first_nm,
                            last_name=last_nm,
                            email=email_str,
                            username=email_str)
            user.save()
            # print(first_name,last_name,email)


