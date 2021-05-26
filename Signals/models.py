from django.db import models
from django.contrib.auth.models import User
from PIL import Image
def upload_Profile_image(instance, filename):
    print("profil;e", filename)
    return "updates/{user}/profile_pics/{filename}".format(user=instance.user, filename=filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to=upload_Profile_image)

    def __str__(self):
        return f'{self.user.username} Profile'