from rest_framework.decorators import (
    api_view,
    permission_classes
)
from .serializers import (
    SubReplySerializer,
    SubReplyActionSerializer
)
from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)
from comments.models import (
    SubReply,
    Reply
)

@api_view(['GET'])
def sub_reply_list(request):
    context = {'request' : request}
    qs = SubReply.objects.all()
    serializer = SubReplySerializer(qs, many=True, context=context)
    return Response(serializer.data, status=200)    

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def sub_reply_details_delete(request, id):
    context = {'request' : request}
    qs = SubReply.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Not found"}, status=404)
    obj = qs.first()
    if request.method == "DELETE" and obj.user == request.user:
        obj.delete()
        return Response({"message" : "Sub Reply successfully deleted"}, status=200)
    serializer = SubReplySerializer(obj, context=context)

    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sub_reply_create(request):
    context = {'request' : request}
    data = request.data
    serializer = SubReplySerializer(data=data, context=context)
    if serializer.is_valid(raise_exception=True):
        replies = Reply.objects.filter(id=int(data.get('reply')))
        if not replies:
            return Response({"message" : "Reply not found"}, status=404)

        obj = replies.first()

        serializer.save(
            user=request.user,
            reply=obj,
        )
        return Response(serializer.data, status=201)

    return Response({}, status=401)

@api_view(['GET'])
def reply_sub_reply_list(request, id):
    context = {'request' : request}
    qs = Reply.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Reply not found"}, status=404)
    obj = qs.first()
    subreplies = SubReply.objects.filter(reply=obj)
    serializer = SubReplySerializer(subreplies, many=True, context=context)
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sub_reply_like_unlike(request):
    context = {'request' : request}
    serializer = SubReplyActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        id = data.get("id")
        action = data.get("action")
        qs = SubReply.objects.filter(id=id)
        if not qs:
            return Response({'message' : 'Sub Reply not found'}, status=404)

        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = SubReplySerializer(obj, context=context)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = SubReplySerializer(obj, context=context)
            return Response(serializer.data, status=200)
    
    return Response({}, status=401)
