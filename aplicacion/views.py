from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import*

# Create your views here.

def home(request):
    return render(request,'aplicacion/home.html')

def experiencias (request):
    contexto={'experiencia':Experiencia.objects.all()}
    return render(request,'aplicacion/experiencia.html',contexto)

def portafolio(request):
    contexto={'portafolio':Portafolio.objects.all()}
    return render(request,'aplicacion/portafolio.html',contexto)

def contacto(request):
    contexto={'contacto':Contacto.objects.all()}
    return render(request,'aplicacion/contacto.html',contexto)


def portafolioForm(request):
    if request.method=="POST":
     portaForm=PortafolioForm(request.POST)
     if portaForm.is_valid():
         porta_nombre=portaForm.cleaned_data.get("nombre")
         porta_lenguaje=portaForm.cleaned_data.get("lenguaje")
         porta_descripcion=portaForm.cleaned_data.get("descripcion")
         portafolio=Portafolio(nombre=porta_nombre,lenguaje=porta_lenguaje,descripcion=porta_descripcion)
         portafolio.save()
         return render(request,"aplicacion/home.html")
    else:
        portaForm=PortafolioForm()
    
    return render(request,'aplicacion/portafolioForm.html',{"form":portaForm})

def contactoForm(request):
    if request.method=="POST":
     portaForm=ContactoForm(request.POST)
     if portaForm.is_valid():
         conta_nombre=portaForm.cleaned_data.get("nombre")
         conta_email=portaForm.cleaned_data.get("email")
         conta_telefono=portaForm.cleaned_data.get("telefono")
         conta_mensaje=portaForm.cleaned_data.get("mensaje")
         contacto=Contacto(nombre=conta_nombre,email=conta_email,telefono=conta_telefono,mensaje=conta_mensaje)
         contacto.save()
         return render(request,"aplicacion/home.html")
    else:
        portaForm=ContactoForm()
    
    return render(request,'aplicacion/portafolioForm.html',{"form":portaForm})
        
    
def experienciaForm(request):
    if request.method=="POST":
     portaForm=ExperienciaForm(request.POST)
     if portaForm.is_valid():
         expe_cargo=portaForm.cleaned_data.get("cargo")
         expe_insti=portaForm.cleaned_data.get("institucion")
         expe_fechaIni=portaForm.cleaned_data.get("fechaDeInicio")
         expe_fechaEgre=portaForm.cleaned_data.get("fechaDeEgreso")
         expe_descripcion=portaForm.cleaned_data.get("descripcion")
         expe_contacto=portaForm.cleaned_data.get("contacto")
         expe_email=portaForm.cleaned_data.get("email")
         experiencia=Experiencia(cargo=expe_cargo,institucion=expe_insti,fechaDeInicio=expe_fechaIni,fechaDeEgreso=expe_fechaEgre,descripcion=expe_descripcion,contacto=expe_contacto,email=expe_email)
         experiencia.save()
         return render(request,"aplicacion/home.html")
    else:
        portaForm=ExperienciaForm()
    
    return render(request,'aplicacion/portafolioForm.html',{"form":portaForm})

def buscar(request):
    return render(request,'aplicacion/buscar.html')

def buscarExperiencia(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        experiencias=Experiencia.objects.filter(cargo__icontains=patron)
        contexto={'experiencia':experiencias}
        return render(request,'aplicacion/experiencia.html',contexto)
    return HttpResponse("No se encontró ninguna experiencia")