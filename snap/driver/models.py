from django.db import models
from snap.users.models import BaseUser


# Create your models here.
class Driver(models.Model):
    car = models.JSONField()
    userid = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
