from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',home,name="home"),
    path('experiencias/',experiencias,name='experiencias'),
    path('portafolio/',PortafolioList.as_view(),name='portafolios'),
    path('contacto/',contacto,name='contactos'),
    
    #Crear portafolio CRUD
    
    path("portafolio_crear/",PortafolioCreate.as_view(),name='portafolio_crear'),
    path("portafolio_update/<int:pk>/",PortafolioUpdate.as_view(),name='portafolio_update'),
    path("portafolio_delete/<int:pk>/",DeletePortafolio.as_view(),name='portafolio_delete'),
   
    
    #Formularios
    path('contactoForm/',contactoForm,name='contactoForm'),
    path('portafolioForm/',portafolioForm,name='portafolioForm'),
    path('experienciaForm/',experienciaForm,name='experienciaForm'),
    
    #Crear y editar Experiencia y eliminar experiencia
    path("experiencia_crear/",createForm,name='experienciaCrear'),
    path("experiencia_actualizar/<id_experiencia>",updateExperiencia,name='experienciaActualizar'),
    path("experiencia_eliminar/<id_experiencia>",deleteExperiencia,name='experienciaBorrar'),

    #Buscar
    
     path('buscar/',buscar,name='buscar'),
     path('buscarExperiencia/',buscarExperiencia,name='buscarExperiencia'),
     
     
     #login,logout,register
    path("login/",login_request,name="login"),
    path("register/",register,name="register"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    
    #Edit profile
    
    path("editarPerfil/",editarPerfil,name="editarPerfil"),
    path("agregarAvatar/",agregarAvatar,name="agregarAvatar")

]

