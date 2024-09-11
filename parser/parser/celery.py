from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser.settings")

app = Celery(
    "celery_app", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
