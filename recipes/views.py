from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "recipes/home.html")

def contato(request):
    return HttpResponse("contato")


def sobre(request):
    return HttpResponse("sobre")

