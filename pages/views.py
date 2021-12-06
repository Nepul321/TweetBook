from django.shortcuts import render

def HomeView(request):
    template = "pages/posts/home.html"
    context = {

    }

    return render(request, template, context)