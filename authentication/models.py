from django.db import models
from django.contrib.auth.models import User
class UserKey(models.Model):
    key = models.CharField(max_length=1000, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activated = models.BooleanField(default=False)