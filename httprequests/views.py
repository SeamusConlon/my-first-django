from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "httprequests/home.html")

def hello(request):
    return render(request, "httprequests/hello.html")