from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def upload_file(instance, filename):
    return "updates/{user}/files/{filename}".format(user=instance.user, filename=filename)


class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_file, null=True, blank=True)
