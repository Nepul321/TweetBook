from django.shortcuts import (
        redirect, 
        render,
)
from django.contrib.auth import (
    login, 
    logout,
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
        AuthenticationForm, 
        PasswordChangeForm
)
from .models import (
    UserKey
)
from .decorators import (
    unauthenticated_user,
    not_active_user
    )
from .forms import (
        AccountForm, 
        SignUpForm
)
from django.contrib.auth.models import User
from src.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

current_host = "http://localhost:8000"

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
        email = request.POST['email']
        qs = User.objects.filter(email=email)
        if form.is_valid() and not qs:
            form.save()
            qs = User.objects.filter(username=request.POST['username'])
            user = qs.first()
            user_key = UserKey.objects.create(
                user=user
            )
            user_key.save()
            user.is_active = False
            user.save()
            subject = "Verify your email"
            message = f"Thanks for signing up. \n Verify your email - {current_host}/accounts/activate-account/{user_key.key}/"
            email_from = EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            template2 = "pages/auth/accounts/email_sent.html"
            context2 = {

            }

            return render(request, template2, context2)


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

@login_required
def PasswordView(request):
	template = "pages/auth/accounts/password.html"
	form = PasswordChangeForm(user=request.user)
	if request.method == "POST":
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('account')

	context = {
        'form' : form
        }
	return render(request, template, context)

@login_required
def DeleteAccountView(request):
    template = "pages/auth/accounts/delete.html"
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        user.delete()
        return redirect('home')
    context = {

    }

    return render(request, template, context)

@not_active_user
def ActivateAccountView(request, token):
        try:
            user = UserKey.objects.get(key=token)
            if user.activated == False:
                user.activated = True
                user.save()
                user.user.is_active = True
                user.user.save()
            else:
                return redirect('/')
        except:
            return redirect('/')
        template = 'pages/auth/accounts/email_verified.html'
        context = {}
        return render(request, template, context)