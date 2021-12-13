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
