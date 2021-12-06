from .views import (
    post_list_view,
    post_detail_view
)

from django.urls import path

urlpatterns = [
    path('', post_list_view, name="post-list"),
    path('<str:id>/', post_detail_view, name="post-detail")
]
