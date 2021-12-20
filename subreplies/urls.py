from django.urls import path
from .views import (
    sub_reply_list
)

urlpatterns = [
    path("", sub_reply_list, name="sub-reply-list"),
]