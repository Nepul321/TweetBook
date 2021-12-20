from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def sub_reply_list(request):
    return Response({"message" : "Sub Reply list"}, status=200)
