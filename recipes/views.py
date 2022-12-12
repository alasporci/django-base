from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "recipes/pages/home.html",context={
        "name": "Nome via contexto"
    })

def contato(request):
    return render(request, "recipes/pages/contato.html")


def sobre(request):
    return render(request, "recipes/pages/sobre.html")

