from comments.serializers import CommentSerializer
from .models import Comment
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.permissions import (
    IsAuthenticated
)

from posts.models import Post

@api_view(['GET'])
def comment_list(request):
    context = {'request' : request}
    qs = Comment.objects.all()
    serializer = CommentSerializer(qs, many=True, context=context)
    return Response(serializer.data, status=200)    

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_details_delete(request, id):
    context = {'request' : request}
    qs = Comment.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Not found"}, status=404)
    obj = qs.first()
    if request.method == "DELETE" and obj.user == request.user:
        obj.delete()
        return Response({"message" : "Comment successfully deleted"}, status=200)
    serializer = CommentSerializer(obj, context=context)

    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request):
    context = {'request' : request}
    data = request.data
    serializer = CommentSerializer(data=data, context=context)
    if serializer.is_valid(raise_exception=True):
        posts = Post.objects.filter(id=int(data.get('post')))
        if not posts:
            return Response({"message" : "Post not found"}, status=404)

        obj = posts.first()

        serializer.save(
            user=request.user,
            post=obj,
        )
        return Response(serializer.data, status=201)

    return Response({}, status=401)

@api_view(['GET'])
def post_comments_list(request, id):
    context = {'request' : request}
    qs = Post.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Post not found"}, status=404)
    obj = qs.first()
    comments = Comment.objects.filter(post=obj)
    serializer = CommentSerializer(comments, many=True, context=context)
    return Response(serializer.data, status=200)