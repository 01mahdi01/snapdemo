from django.db import models
from snap.users.models import BaseUser
from snap.driver.models import Driver


class Ride(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.DO_NOTHING)
    driver = models.OneToOneField(Driver, on_delete=models.DO_NOTHING)
    log = models.JSONField
