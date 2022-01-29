import os
from celery import Celery
from celery.schedules import crontab


from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_ex.settings")

app = Celery("test_ex")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "reset_upvotes": {
        "task": "posts.tasks.reset_upvotes",
        "schedule": crontab(hour=0, minute=0),
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f"Request:{self.request!r}")
