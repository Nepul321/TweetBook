from django.urls import path
from .views import (
    DeleteAccountView,
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
    path('delete/', DeleteAccountView, name="delete"),
]
