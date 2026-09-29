from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def hellos(request, nombre):
    return HttpResponse(f"<h1>Hello {nombre}</h1>")

def about(request):
    return HttpResponse('About')