from rest_framework import serializers
from comments.models import Reply
from posts.serializers import UserPublicSerializer

REPLY_VALIDATE = ['like', 'unlike']

class ReplySerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Reply
        fields = ('id', 'content', 'user', 'date', 'is_owner', 'likes')

    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.user == request.user:
                return True
        return False

    def get_likes(self, obj):
        return obj.likes.count()

class ReplyActionSerializer(serializers.Serializer):
    id = serializers.CharField()
    action = serializers.CharField()
    def validate_action(self, value):
        value = value.lower().strip()
        if value not in REPLY_VALIDATE:
            raise serializers.ValidationError("This is not a valid action")
        return value