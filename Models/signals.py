from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Temp


@receiver(post_delete, sender=Temp, dispatch_uid="postDelete")
def postDelete(sender, instance, **kwargs):
    print("Executing post delete")
