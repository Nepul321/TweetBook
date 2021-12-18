from rest_framework import serializers
from .models import (
    Comment,
    # Reply,
    # SubReply
)

from posts.serializers import UserPublicSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user')