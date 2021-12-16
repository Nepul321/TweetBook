from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.decorators import (
    api_view,
    permission_classes
)

from profiles.serializers import ProfileSerializer
from .models import Profile

@api_view(['GET'])
def ProfileList(request):
    context = {'request' : request}
    qs = Profile.objects.all()
    serializer = ProfileSerializer(qs, many=True, context=context)

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def ProfileDetail(request, username):
    context = {'request' : request}
    qs = Profile.objects.filter(user__username__iexact=username)
    if not qs.exists():
        return Response({"details" : "Profile not found"}, status=404)
    obj = qs.first()
    data = request.data or {}
    if request.method == "POST":
        me = request.user
        action = data.get('action')
        if obj.user != me:
            if action == "follow":
                if me.is_authenticated == True:
                    obj.followers.add(me)
            elif action == "unfollow":
                if me.is_authenticated == True:
                    obj.followers.remove(me)
            else:
                pass
    serializer = ProfileSerializer(instance=obj, context=context)

    return Response(serializer.data, status=200)
