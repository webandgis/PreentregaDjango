from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('experiencias/',experiencias,name='experiencias'),
    path('portafolio/',portafolio,name='portafolios'),
    path('contacto/',contacto,name='contactos'),
    
    #Formularios
    path('portafolioForm/',portafolioForm,name='portafolioForm'),
    path('contactoForm/',contactoForm,name='contactoForm'),
    path('experienciaForm/',experienciaForm,name='experienciaForm'),
    
    #Buscar
    
     path('buscar/',buscar,name='buscar'),
     path('buscarExperiencia/',buscarExperiencia,name='buscarExperiencia'),

]
