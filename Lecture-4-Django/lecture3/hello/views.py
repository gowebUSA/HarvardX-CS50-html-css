from django.http import HttpResponse    #import the ability fro HttpResponse.This is like using Using Statement in C#
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world!")

# def richard(request):
#     return HttpResponse("Hello, Richard!")

# def ruby(request):
#     return HttpResponse("Hello, Ruby!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}")

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def richard(request):
    return HttpResponse("Hello, Richard!")

def ruby(request):
    return HttpResponse("Hello, Ruby!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":  name.capitalize()   #this is a python dictionary, key/value pair
    })