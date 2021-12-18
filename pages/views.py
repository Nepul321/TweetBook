from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from profiles.forms import ProfileForm
from profiles.models import Profile
from django.contrib.auth.decorators import login_required

def HomeView(request):
    template = "pages/posts/home.html"
    context = {

    }

    return render(request, template, context)

def DetailView(request, pk):
    template = "pages/posts/details.html"
    context = {
     'id' : pk,
    }

    return render(request, template, context)

def ProfilePage(request, username):
    template = "pages/profiles/profile.html"
    obj = username
    context = {
      'profile' : obj,
    }

    return render(request, template, context)

@login_required
def ProfileEdit(request):
    template = "pages/profiles/profile-update.html"
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-edit')
    context = {
      'form' : form,
      'profile' : profile,
    }

    return render(request, template, context)

def UserPostsView(request, username):
    template = "pages/posts/user_posts.html"
    qs = User.objects.filter(username=username)
    if qs:
        obj = qs.first()
    else:
        return redirect('/')
    context = {
        'username' : obj.username or '',
    }

    return render(request, template, context)