from django.contrib.auth.models import User
from django.db import models
from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name="comment_likes")
    content = models.TextField(max_length=240)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']

class Reply(models.Model):
    comment = models.ForeignKey(Comment, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name="reply_likes")
    content = models.TextField(max_length=240)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']

class SubReply(models.Model):
    reply = models.ForeignKey(Reply, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name="subreply_likes")
    content = models.TextField(max_length=240)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']