from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class testy():
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def conc():
        return str(self.name)+str(self.number)

def home(request):
    return render(request, "httprequests/home.html")

def hello(request):
    the_name = request.GET.get('name')
    the_number = request.GET.get('number')
    test = testy(the_name,the_number)
    return render(request, "httprequests/hello.html", {'name':the_name,'number':the_number})