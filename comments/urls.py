from django.urls import path
from .views import (
    comment_create,
    comment_details_delete,
    comment_list,
    post_comments_list
)

urlpatterns = [
    path('', comment_list, name="comments"),
    path("<int:id>/", comment_details_delete, name="comment-details"),
    path('create/', comment_create, name="comment-create"),
    path('post/<int:id>/', post_comments_list, name="post-comments-list"),
]
