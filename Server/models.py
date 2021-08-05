from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Server(models.Model):
    # users = models.ManyToManyField(User)
    server_name = models.CharField(max_length=32)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.server_name} Server'


class ServerList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    # server = models.ManyToManyField(Server)

    class Meta:
        unique_together = (('user', 'server'),)

    def __str__(self):
        return f'User: {self.user.username} / Server: {self.server.server_name}'

