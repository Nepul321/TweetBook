from django.urls import path
from .views import (
    comment_list
)

urlpatterns = [
    path('', comment_list, name="comments"),
]
