# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)





app.conf.beat_schedule = {
    'update-exchange-rates': {
        'task': 'currency_converter.tasks.update_exchange_rates',
        'schedule': 30.0,  # Every 30 seconds
    },
}