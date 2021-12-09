from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
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
