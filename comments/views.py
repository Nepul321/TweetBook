from comments.serializers import CommentSerializer
from .models import Comment
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    # permission_classes
)
# from rest_framework.permissions import (
#     IsAuthenticated
# )

@api_view(['GET'])
def comment_list(request):
    context = {'request' : request}
    qs = Comment.objects.all()
    serializer = CommentSerializer(qs, many=True, context=context)
    return Response(serializer.data, status=200)    

@api_view(['GET'])
def comment_details(request, id):
    context = {'request' : request}
    qs = Comment.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Not found"})
    obj = qs.first()
    serializer = CommentSerializer(obj, context=context)

    return Response(serializer.data, status=200)