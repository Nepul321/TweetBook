from django.shortcuts import redirect, render
from profiles.models import Profile

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