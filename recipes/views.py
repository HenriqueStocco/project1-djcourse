from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')


def about(request):
    return HttpResponse('ABOUT')


def contact(request):
    return HttpResponse('CONTACT')
