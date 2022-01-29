from celery import shared_task
from posts.models import Post


@shared_task
def reset_upvotes():
    Post.objects.filter(amount_of_upvotes__gt=0).update(amount_of_upvotes=0)
