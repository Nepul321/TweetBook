from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from .models import Post
from .serializers import PostSerializer
# from rest_framework.permissions import (
#     IsAuthenticated
# )
from rest_framework.response import Response

@api_view(['GET'])
def post_list_view(request):
    context = {'request' : request}
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True, context=context)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def post_detail_view(request, id):
    context = {'request' : request}
    qs = Post.objects.filter(id=id)
    if not qs.exists():
        return Response({'message' : 'Object not found'}, status=404)
    obj = qs.first()
    serializer = PostSerializer(obj, context=context)
    return Response(serializer.data, status=200)