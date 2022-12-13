from django.urls import path
from . import views

# teste 
# from django.http import HttpResponse

# def my_views(request):
#     return HttpResponse("um string")


urlpatterns = [
    path('', views.home),
    path('contato/', views.contato),
    path('sobre/', views.sobre),
    path('recipes/<int:id>/', views.recipe),
]
