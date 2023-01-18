from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppTerceraEntrega.models import Futbol, Tenis, Voley, Handball, Deportista
from AppTerceraEntrega.forms import DeportistasFormulario, Futbolistas, Voleybolistas, Tenistas, Handballistas
from AppTerceraEntrega.forms import DeportistasFormulario
from AppTerceraEntrega import models
# Create your views here.

def inicio(request):
    return render(request, "AppTerceraEntrega/inicio.html")

def deportista(self):
    deportista = Deportista(nombre="Mariano", apellido="Fogel", altura=1.81, deporte="Handball")
    deportista.save()
    doc = f"El deportiste {deportista.nombre} {deportista.apellido} viene para jugar al {deportiste.deporte}"
    return HttpResponse(doc)

def futbol(request):
    if request.method == 'POST':
            
            miFormulario = Futbolistas(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  futbolista = Futbol(nombre=informacion['nombre'], apellido=informacion['apellido'], posicion=informacion['posicion'], contacto=informacion['contacto']) 
                  futbolista.save()
                  return render(request, "AppTerceraEntrega/inicio.html") #Vuelvo al inicio o a donde quieran
    else: 
        miFormulario= Futbolistas() #Formulario vacio para construir el html

    return render(request, "AppTerceraEntrega/futbol.html", {"miFormulario":miFormulario})

def voley(request):
    if request.method == 'POST':
            
            miFormulario = Voleybolistas(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  voleyballista = Voley(nombre=informacion['nombre'], apellido=informacion['apellido'], altura=informacion['altura'], contacto=informacion['contacto']) 
                  voleyballista.save()
                  return render(request, "AppTerceraEntrega/inicio.html") #Vuelvo al inicio o a donde quieran
    else: 
        miFormulario= Voleybolistas() #Formulario vacio para construir el html

    return render(request, "AppTerceraEntrega/voley.html", {"miFormulario":miFormulario})

def handball(request):
    if request.method == 'POST':
            
            miFormulario = Handballistas(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  handballista = Handball(nombre=informacion['nombre'], apellido=informacion['apellido'], altura=informacion['altura'], contacto=informacion['contacto']) 
                  handballista.save()
                  return render(request, "AppTerceraEntrega/inicio.html") #Vuelvo al inicio o a donde quieran
    else: 
        miFormulario= Handballistas() #Formulario vacio para construir el html

    return render(request, "AppTerceraEntrega/handball.html", {"miFormulario":miFormulario})

def tenis(request):
    if request.method == 'POST':
            
            miFormulario = Tenistas(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  tenista = Tenis(nombre=informacion['nombre'], apellido=informacion['apellido'], mano_habil=informacion['mano_habil'], contacto=informacion['contacto']) 
                  tenista.save()
                  return render(request, "AppTerceraEntrega/inicio.html") #Vuelvo al inicio o a donde quieran
    else: 
        miFormulario= Tenistas() #Formulario vacio para construir el html

    return render(request, "AppTerceraEntrega/tenis.html", {"miFormulario":miFormulario})


def deportistasFormulario(request):
    if request.method == "POST":
        
        miFormulario = DeportistasFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            deportista = Deportista(nombre=informacion["nombre"], apellido=informacion["apellido"], altura=informacion["altura"], deporte=informacion["deporte"])
            deportista.save()
            
            return render(request, "AppTerceraEntrega/inicio.html")
        
        else:
            miFormulario = DeportistasFormulario()
            
    return render(request, "AppTerceraEntrega/deportistasFormulario.html", {"miFormulario": DeportistasFormulario})

def buscarDeporte(request):
    return render(request, "AppTerceraEntrega/buscarDeporte.html")

def busqueda(request):
    respuesta = f"Estoy buscando el deporte: {request.GET['deporte']}"
    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)
