from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from profiles.forms import ProfileForm
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from posts.models import (
    Post
)
from comments.models import (
    Comment,
    Reply
)

def HomeView(request):
    template = "pages/posts/home.html"
    context = {

    }

    return render(request, template, context)

def DetailView(request, pk):
    template = "pages/posts/details.html"
    qs = Post.objects.filter(id=pk)
    if not qs:
        return redirect('/')

    obj = qs.first()
    context = {
     'id' : obj.id,
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

def RepliesView(request, id):
    template = "pages/replies/replies.html"
    qs = Comment.objects.filter(id=id)
    if not qs:
        return redirect('/')

    obj = qs.first()
    context = {
        'obj' : obj,
    }

    return render(request, template, context)

def SubRepliesView(request, id):
    template = "pages/subreplies/subreplies.html"
    qs = Reply.objects.filter(id=id)
    if not qs:
        return redirect('/')

    obj = qs.first()
    context = {
      'obj' : obj,
    }

    return render(request, template, context)