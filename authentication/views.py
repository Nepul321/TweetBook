from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .decorators import unauthenticated_user
from .forms import (
        AccountForm, 
        SignUpForm
)

@unauthenticated_user
def LoginView(request):
    template = "pages/auth/login.html"
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
       'form' : form,
    }
    return render(request, template, context)

@login_required
def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('accounts-login')
    else:
        return redirect('home')

@unauthenticated_user
def SignUpView(request):
    template = "pages/auth/registration/signup.html"
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts-login')
    context = {
       'form' :  form,
    }

    return render(request, template, context)

@login_required
def AccountView(request):
    template = "pages/auth/accounts/account.html"
    form = AccountForm(instance=request.user)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {
     'form' : form,
    }

    return render(request, template, context)