from django.shortcuts import render

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