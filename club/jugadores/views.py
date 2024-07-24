from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Jugador
from .forms import  JugadorForm

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")
def nosotros(request):
     return render(request, "paginas/nosotros.html")
def jugadores(request):
    jugadores=jugadores.objects.all()
    #print(jugadores)
    return render(request, "crud/index.html",{"jugadores":jugadores})
def crear(request):
    formulario=JugadorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return render