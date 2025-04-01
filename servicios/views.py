from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

def servicios(request):
    servicios = Servicio.objects.all()  
    return render(request, "servicios/servicios.html", {'servicios':servicios})
