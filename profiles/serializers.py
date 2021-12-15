from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    # image_url = serializers.SerializerMethodField(read_only=True)
    followers = serializers.SerializerMethodField(read_only=True)
    following = serializers.SerializerMethodField(read_only=True)
    is_following = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'username', 'image', 'followers', 'following', 'bio', 'location', 'is_following', 'name', 'joined')

    # def get_image_url(self, obj):
    #     image = ''
    #     return image

    def get_followers(self, obj):
        return obj.followers.count()

    def get_following(self, obj):
        return obj.user.following.count()

    def get_is_following(self, obj):
        is_following = False
        context  = self.context
        request = context.get("request")
        if request:
            user = request.user
            is_following = user in obj.followers.all()
        return is_following

    def get_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def get_username(self, obj):
        return obj.user.username        