from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from .models import Post
from .serializers import (
    PostCreateSerializer,
    PostSerializer,
    PostActionSerializer
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.response import Response

@api_view(['GET'])
def post_list_view(request):
    context = {'request' : request}
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True, context=context)
    return Response(serializer.data, status=200)

@api_view(['GET', 'POST', 'DELETE'])
def post_detail_view(request, id):
    context = {'request' : request}
    qs = Post.objects.filter(id=id)
    if not qs.exists():
        return Response({'message' : 'Object not found'}, status=404)
    obj = qs.first()
    if request.method == "POST" and obj.user == request.user:
        serializer = PostCreateSerializer(instance=obj, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
    if request.method == "DELETE" and obj.user == request.user:
        obj.delete()
        return Response({'message' : "Post successfully deleted"}, status=200)
    serializer = PostSerializer(obj, context=context)
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create_view(request):
    serializer = PostCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    
    return Response({}, status=401)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_like_unlike_view(request):
    context = {"request" : request}
    serializer = PostActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        id = data.get("id")
        action = data.get("action")
        qs = Post.objects.filter(id=id)
        if not qs.exists():
            return Response({}, status=404)

        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = PostSerializer(obj, context=context)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = PostSerializer(obj, context=context)
            return Response(serializer.data, status=200)

    return Response({}, 200)




    