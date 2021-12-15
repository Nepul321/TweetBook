from django.urls import path
from .views import (
    DetailView,
    HomeView,
    ProfilePage
)

urlpatterns = [
    path('', HomeView, name="home"),
    path('<int:pk>/', DetailView, name="details"),
    path('profile/<str:username>/', ProfilePage, name="profile"),
]
