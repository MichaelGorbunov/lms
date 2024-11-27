import random

from django.core.management.base import BaseCommand
from unidecode import unidecode

from users.models import CustomUser


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):

        fname = ["Петр", "Иван", "Сергей", "Антон"]
        lname = ["Иванов", "Петров", "Сергеев", "Васин", "Антонов"]
        for m in range(19):
            first_nm = random.choice(fname)
            last_nm = random.choice(lname)
            email_str = str(m + 1) + unidecode(first_nm + last_nm) + "@lms.ru"

            user = CustomUser(
                first_name=first_nm,
                last_name=last_nm,
                email=email_str,
                username=email_str,
            )
            user.set_password("123456789")
            user.save()
            # print(first_name,last_name,email)
