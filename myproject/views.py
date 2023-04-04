from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, "myproject/index.html")
def greet(request, name):
    return render(request, "myproject/greet.html",{
        "name": name.capitalize()
         })
def world(request):
    return HttpResponse("Hello People !")
def sugyan(request):
    return HttpResponse("Hello, Sugyan! How is your day Today?")
                        