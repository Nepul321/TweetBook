from django.contrib.auth.models import User
from django.urls import path
from .views import (
    DetailView,
    HomeView,
    ProfileEdit,
    ProfilePage,
    UserPostsView
)

urlpatterns = [
    path('', HomeView, name="home"),
    path('<int:pk>/', DetailView, name="details"),
    path('profile/<str:username>/', ProfilePage, name="profile"),
    path('profile/', ProfileEdit, name="profile-edit"),
    path('posts/<str:username>/', UserPostsView, name="user-posts")
]
