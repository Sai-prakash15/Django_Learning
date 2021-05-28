from django.db import models
from django.contrib.auth.models import User


def upload_Status_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


# Create your models here.

class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):  # fb status, instagram post, tweet etc
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_Status_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:20]

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
