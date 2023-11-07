from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'pages/home.html', status=200, context={
        'name': 'Adrian and Simon',
    })


def about(request):
    return HttpResponse('ABOUT')


def contact(request):
    return HttpResponse('CONTACT')
