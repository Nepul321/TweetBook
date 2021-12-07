from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'username',  
            'first_name',
            'last_name',
        ]
class PostCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'content', 'likes', 'user')

    def get_likes(self, obj):
        return obj.likes.count()

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ('content', 'user', 'likes', 'timestamp', 'is_owner')

    def get_likes(self, obj):
        return obj.likes.count()
        
    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.user == request.user:
                return True
        return False
