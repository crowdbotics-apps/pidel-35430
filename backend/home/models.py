from django.conf import settings
from django.db import models


class Login(models.Model):
    "Generated Model"
    userid = models.BigIntegerField()
    password = models.BigIntegerField()
