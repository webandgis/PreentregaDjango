from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import *
from .forms import*

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'aplicacion/home.html')

@login_required
def experiencias (request):
    contexto={'experiencia':Experiencia.objects.all()}
    return render(request,'aplicacion/experiencia.html',contexto)

@login_required
def portafolio(request):
    contexto={'portafolio':Portafolio.objects.all()}
    return render(request,'aplicacion/portafolios.html',contexto)
@login_required
def contacto(request):
    contexto={'contacto':Contacto.objects.all()}
    return render(request,'aplicacion/contacto.html',contexto)
#___________________________________________Formularios
@login_required
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
@login_required
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

#_________________________________________Crear Formulario        
@login_required  
def createForm(request):
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
         return redirect(reverse_lazy('experiencias'))
    else:
        portaForm=ExperienciaForm()
    
    return render(request,'aplicacion/portafolioForm.html',{"form":portaForm})
@login_required  
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
    
    return render(request,'aplicacion/experienciaForm.html',{"form":portaForm})

@login_required
def buscar(request):
    return render(request,'aplicacion/buscar.html')
@login_required
def buscarExperiencia(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        experiencias=Experiencia.objects.filter(cargo__icontains=patron)
        contexto={'experiencia':experiencias}
        return render(request,'aplicacion/experiencia.html',contexto)
    return HttpResponse("No se encontró ninguna experiencia")
#____________________________________________Updateexperiencia
@login_required
def updateExperiencia(request, id_experiencia):
    experiencia = get_object_or_404(Experiencia, id=id_experiencia)
    if request.method == "POST":
        portaForm = ExperienciaForm(request.POST, instance=experiencia)
        if portaForm.is_valid():
            portaForm.save()
            return redirect(reverse_lazy('experiencias'))
    else:
        portaForm = ExperienciaForm(instance=experiencia)
    return render(request, 'aplicacion/experienciaForm.html', {'form': portaForm})    

#_______________________________________Delete Experiencia
@login_required
def deleteExperiencia(request,id_experiencia):
    experiencia=Experiencia.objects.get(id=id_experiencia)
    experiencia.delete()
    return redirect(reverse_lazy('experiencias'))

#______________________________________________Clases Portafolio

class PortafolioList(LoginRequiredMixin,ListView):
    model=Portafolio

class PortafolioCreate(LoginRequiredMixin,CreateView):
    model=Portafolio
    fields=['nombre','lenguaje','descripcion']
    success_url=reverse_lazy('portafolios')
    
class PortafolioUpdate(LoginRequiredMixin,UpdateView):
    model=Portafolio
    fields=['nombre','lenguaje','descripcion']
    success_url=reverse_lazy('portafolios')

class DeletePortafolio(LoginRequiredMixin,DeleteView):
    model=Portafolio
    success_url=reverse_lazy('portafolios')
    
#______________________________________________Login,Logout
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________

            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm })    
#____________________________________Registro
def register(request):
    if request.method=="POST":
     portaForm=RegistroForm(request.POST)
     if portaForm.is_valid():
         usuario=portaForm.cleaned_data.get("username")
         portaForm.save()
        
         
         return redirect(reverse_lazy("home"))
    else:
        portaForm=RegistroForm()
    
    return render(request,'aplicacion/register.html',{"form":portaForm})

#______________________________________Editar Perfil
@login_required
def editarPerfil(request):
 usuario=request.user
 if request.method=="POST":
  form=UserEditForm(request.POST)
  if form.is_valid():
   info=form.cleaned_data
   usuario=User.objects.get(username=usuario)
   usuario.email=info['email']
   usuario.nombre=info['nombre']
   usuario.apellido=info['apellido']
   usuario.set_password(['password1'])
   usuario.save()
   messages.success(request,"Se ha actualizado su perfil de manera exitosa")
        
         
  return render(request,"aplicacion/home.html")
 else:
  form=UserEditForm(instance=usuario)
    
 return render(request,'aplicacion/editarPerfil.html',{"form":form})  

#_______________________________________________Añadir Avatar      
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
         
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/home.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form })   
        