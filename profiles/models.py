from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="profiles-pics/")
    location = models.CharField(blank=True, max_length=100)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name="following")
