from django.shortcuts import render, HttpResponse
from utilidades import funciones



# Create your views here.


def Devuelve(request):
    response = 'Hola maja, te devuelvo .... '
    response += funciones.DevuelveCuatro('Lo que sea que te de')
    return HttpResponse(response)
