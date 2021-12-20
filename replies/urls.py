from django.urls import path
from .views import (
    comments_reply_list,
    reply_create,
    reply_details_delete,
    reply_like_unlike,
    reply_list
)

urlpatterns = [
    path("", reply_list, name="reply-list"),
    path("<int:id>/", reply_details_delete, name="reply-detail-delete"),
    path("create/", reply_create, name="reply-create"),
    path('like-unlike/', reply_like_unlike, name="reply-like-unlike"),
    path('comment/<int:id>/', comments_reply_list, name="comment-reply-list"),
]
