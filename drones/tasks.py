from celery import shared_task
from datetime import datetime



@shared_task
def periodic_task():
    for i in range(10):
        print(i)
    print("Task ended:", datetime.now())
