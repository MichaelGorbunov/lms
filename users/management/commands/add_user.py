import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from users.models import CustomUser, Payments


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Payments.objects.all().delete()
        # CustomUser.objects.all().delete()
        #
        # call_command(
        #     "loaddata", os.path.join(settings.BASE_DIR, "data", "users_fixture.json")
        # )
        call_command(
            "loaddata", os.path.join(settings.BASE_DIR, "data", "payments_fixture.json")
        )
