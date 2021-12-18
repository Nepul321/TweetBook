from django.urls import path
from .views import (
    comment_details,
    comment_list
)

urlpatterns = [
    path('', comment_list, name="comments"),
    path("<int:id>/", comment_details, name="comment-details"),
]
