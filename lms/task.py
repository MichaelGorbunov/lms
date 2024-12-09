from celery import shared_task


@shared_task
def add_numbers():
    print("x + y")

