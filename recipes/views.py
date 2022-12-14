from django.shortcuts import render
from fakerdata.main import makedata

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "recipes/pages/home.html", context={
        'recipes':[makedata() for _ in range(10)]})

def contato(request):
    return render(request, "recipes/pages/contato.html")


def sobre(request):
    return render(request, "recipes/pages/sobre.html")

def recipe(request,id):
    return render(request, "recipes/pages/recipe.html", context={
        'recipe':makedata(),
    })

    