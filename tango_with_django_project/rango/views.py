from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = "Rango says hey there partner! " + "<a href='/rango/about/'>About</a>"
    return HttpResponse(html)


def about(request):
    html = "Rango says here is the about page." + "<a href='/'>Index</a>"
    return HttpResponse(html)
