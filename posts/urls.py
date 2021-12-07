from .views import (
    post_like_unlike_view,
    post_list_view,
    post_detail_view,
    post_create_view
)

from django.urls import path

urlpatterns = [
    path('', post_list_view, name="post-list"),
    path('<int:id>/', post_detail_view, name="post-detail"),
    path('create/', post_create_view, name="post-create"),
    path('action/', post_like_unlike_view, name="post-like-unlike"),
]
