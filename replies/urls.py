from django.urls import path
from .views import (
    reply_list
)

urlpatterns = [
    path("", reply_list, name="reply-list"),
]
