from .views import (
    post_list_view,
    post_detail_view,
    post_create_view
)

from django.urls import path

urlpatterns = [
    path('', post_list_view, name="post-list"),
    path('post/<str:id>/', post_detail_view, name="post-detail"),
    path('posts/create/', post_create_view, name="post-create"),
]
