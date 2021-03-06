import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsfeed_portal.settings')

app = Celery('newsfeed_portal')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'fetch-every-10-minutes': {
        'task': 'news.tasks.fetch_news',
        'schedule': crontab(minute="*/10"), # a job is scheduled to run every 10 minutes
        'args': ()
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()