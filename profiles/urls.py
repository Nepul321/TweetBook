from django.urls import path
from .views import (
    ProfileList
)

urlpatterns = [
    path('', ProfileList, name="profile-list"),
]
