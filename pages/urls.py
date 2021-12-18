from django.urls import path
from .views import (
    DetailView,
    HomeView,
    ProfileEdit,
    ProfilePage
)

urlpatterns = [
    path('', HomeView, name="home"),
    path('<int:pk>/', DetailView, name="details"),
    path('profile/<str:username>/', ProfilePage, name="profile"),
    path('profile/', ProfileEdit, name="profile-edit"),
]
