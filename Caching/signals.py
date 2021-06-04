from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Recipe
from django_redis import get_redis_connection
from django.db import transaction
from django.core.cache import cache


@receiver([post_save, post_delete], sender=Recipe, dispatch_uid="clear_fancy_cache")
def clear_fancy_cache(sender, instance, **kwargs):
    list_of_models = ('Recipe')
    print("caching clear signal")
    if sender.__name__ in list_of_models:
        transaction.on_commit(
            # lambda: get_redis_connection("default").flushall()
            lambda: cache.clear()
        )