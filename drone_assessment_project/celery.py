import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drone_assessment_project.settings')

app = Celery('drone_assessment_project')
app.conf.enable_utc = False

app.config_from_object('drone_assessment_project.settings', namespace='CELERY')

app.autodiscover_tasks()


