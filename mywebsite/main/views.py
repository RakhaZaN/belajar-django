from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello World !</h1>")

def otherView(response):
    return HttpResponse("<h1>You are in another page</h1>")