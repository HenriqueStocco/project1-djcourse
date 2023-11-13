from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/home.html', status=200)


def recipe(request, id):
    return render(request, 'pages/recipe-view.html', status=200)
