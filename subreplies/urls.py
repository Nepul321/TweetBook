from django.urls import path
from .views import (
    reply_sub_reply_list,
    sub_reply_create,
    sub_reply_details_delete,
    sub_reply_like_unlike,
    sub_reply_list
)

urlpatterns = [
    path("", sub_reply_list, name="sub-reply-list"),
    path("<int:id>/", sub_reply_details_delete, name="sub-reply-detail-delete"),
    path("create/", sub_reply_create, name="sub-reply-create"),
    path("reply/<int:id>/", reply_sub_reply_list, name="reply-sub-reply-list"),
    path("like-unlike/", sub_reply_like_unlike, name="sub-reply-like-unlike")
]