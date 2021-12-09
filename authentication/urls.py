from django.urls import path
from .views import (
    LoginView,
    LogoutView
)

urlpatterns = [
    path('login/', LoginView, name="accounts-login"),
    path('logout/', LogoutView, name="accounts-logout")
]
