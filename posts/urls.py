from .views import (
    post_list_view
)

from django.urls import path

urlpatterns = [
    path('', post_list_view, name="post-list"),
]
