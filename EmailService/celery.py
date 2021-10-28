from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery

# setting the Django settings module
os.environ.get('DJANGO_SETTINGS_MODULE', 'EmailService.settings')
app = Celery('EmailService')
app.config_from_object('django.conf:settings', namespace='CELERY')


# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)