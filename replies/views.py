from rest_framework.decorators import (
    api_view,
    permission_classes
)
from .serializers import (
    ReplySerializer,
    ReplyActionSerializer
)
from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)
from comments.models import (
    Reply,
    Comment
)

@api_view(['GET'])
def reply_list(request):
    context = {'request' : request}
    qs = Reply.objects.all()
    serializer = ReplySerializer(qs, many=True, context=context)
    return Response(serializer.data, status=200)    

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def reply_details_delete(request, id):
    context = {'request' : request}
    qs = Reply.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Not found"}, status=404)
    obj = qs.first()
    if request.method == "DELETE" and obj.user == request.user:
        obj.delete()
        return Response({"message" : "Reply successfully deleted"}, status=200)
    serializer = ReplySerializer(obj, context=context)

    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reply_create(request):
    context = {'request' : request}
    data = request.data
    serializer = ReplySerializer(data=data, context=context)
    if serializer.is_valid(raise_exception=True):
        comments = Comment.objects.filter(id=int(data.get('comment')))
        if not comments:
            return Response({"message" : "Comment not found"}, status=404)

        obj = comments.first()

        serializer.save(
            user=request.user,
            comment=obj,
        )
        return Response(serializer.data, status=201)

    return Response({}, status=401)

@api_view(['GET'])
def comments_reply_list(request, id):
    context = {'request' : request}
    qs = Comment.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Comment not found"}, status=404)
    obj = qs.first()
    replies = Reply.objects.filter(post=obj)
    serializer = ReplySerializer(replies, many=True, context=context)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def reply_like_unlike(request):
    context = {'request' : request}
    serializer = ReplyActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        id = data.get("id")
        action = data.get("action")
        qs = Reply.objects.filter(id=id)
        if not qs:
            return Response({'message' : 'Reply not found'}, status=404)

        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = ReplySerializer(obj, context=context)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = ReplySerializer(obj, context=context)
            return Response(serializer.data, status=200)
    
    return Response({}, status=401)
