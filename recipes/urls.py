from django.urls import path
from recipes.views import home, contato, sobre

# teste 
# from django.http import HttpResponse

# def my_views(request):
#     return HttpResponse("um string")


urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
