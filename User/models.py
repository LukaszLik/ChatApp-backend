from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from backend.static import USER_STATUS


# Create your models here.
class Status(models.Model):
    status = models.PositiveSmallIntegerField(choices=USER_STATUS)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=USER_STATUS, default=5)
    profile_picture = models.ImageField(default='default.jpg', upload_to='pfp')
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 250 or img.width > 250:
            img.thumbnail((250, 250))
            img.save(self.profile_picture.path)
