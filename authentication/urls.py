from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    SignUpView,
    AccountView
)

urlpatterns = [
    path('login/', LoginView, name="accounts-login"),
    path('logout/', LogoutView, name="accounts-logout"),
    path('sign-up/', SignUpView, name="signup"),
    path('account/', AccountView, name="account"),
]
