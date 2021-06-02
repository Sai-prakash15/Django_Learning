from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Recipe
from django_redis import get_redis_connection


@receiver(post_save, sender=Recipe, dispatch_uid="clear_fancy_cache")
def clear_fancy_cache(sender, instance, **kwargs):
    print("here")
    get_redis_connection("default").flushall()
