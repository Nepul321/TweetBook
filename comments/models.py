from django.contrib.auth.models import User
from django.db import models
from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=240)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=240)

class SubReply(models.Model):
    reply = models.ForeignKey(Reply, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=240)