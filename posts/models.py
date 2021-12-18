from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField(max_length=250)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return "Post " + str(self.id)