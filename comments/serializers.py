from rest_framework import serializers
from .models import (
    Comment,
    # Reply,
    # SubReply
)

from posts.serializers import UserPublicSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'date', 'is_owner', 'likes')

    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.user == request.user:
                return True
        return False

    def get_likes(self, obj):
        return obj.likes.count()
