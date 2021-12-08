from django.urls import path
from .views import (
    DetailView,
    HomeView
)

urlpatterns = [
    path('', HomeView, name="home"),
    path('<int:pk>/', DetailView, name="details"),
]
