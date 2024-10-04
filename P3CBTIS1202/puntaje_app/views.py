from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request,"index.html")

def jaulas (request):
    return render(request,"jaulas.html")

def empleados(request):
    return render(request, "empleados.html")

def perros(request):
    return render(request, "perros.html")

def adoptantes(request):
    return render(request, "adoptantes.html")

