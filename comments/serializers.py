from rest_framework import serializers
from .models import (
    Comment,
    # Reply,
    # SubReply
)

from posts.serializers import UserPublicSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer()
    is_owner = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'date', 'is_owner')

    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.user == request.user:
                return True
        return False
