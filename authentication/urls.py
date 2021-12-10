from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    PasswordView,
    SignUpView,
    AccountView
)

urlpatterns = [
    path('login/', LoginView, name="accounts-login"),
    path('logout/', LogoutView, name="accounts-logout"),
    path('sign-up/', SignUpView, name="signup"),
    path('account/', AccountView, name="account"),
    path('password/', PasswordView, name="password"),
]
