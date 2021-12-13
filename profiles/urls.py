from django.urls import path
from .views import (
    ProfileDetail,
    ProfileList
)

urlpatterns = [
    path('', ProfileList, name="profile-list"),
    path('<str:username>/', ProfileDetail, name="profile-detail"),
]
