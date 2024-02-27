from django import forms
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PortafolioForm(forms.Form):
    nombre=forms.CharField(max_length=50,required=True)
    lenguaje=forms.CharField(max_length=50,required=True)
    descripcion=forms.CharField(max_length=100,required=True)

class ContactoForm(forms.Form):
    nombre=forms.CharField(max_length=50,required=True)
    email=forms.EmailField(required=True)
    telefono=forms.IntegerField(required=True)
    mensaje=forms.CharField(max_length=100,required=True)
    
class ExperienciaForm(forms.ModelForm):
    cargo=forms.CharField(max_length=50)
    institucion=forms.CharField(max_length=50)
    fechaDeInicio=forms.DateField()
    fechaDeEgreso=forms.DateField()
    descripcion=forms.CharField(max_length=100)
    contacto=forms.CharField(max_length=50)
    email=forms.EmailField()
    
    class Meta:
        model = Experiencia
        fields = '__all__'

class RegistroForm(UserCreationForm):
     email=forms.EmailField(max_length=50,required=True)
     password1=forms.CharField(label="Contraseña",max_length=50,required=True,widget=forms.PasswordInput)
     password2=forms.CharField(label="Confirmar Contraseña",required=True,widget=forms.PasswordInput)
     
     class Meta:
         model=User
         fields=['username','email','password1','password2']

class UserEditForm(UserCreationForm):
     email=forms.EmailField(max_length=50,required=True)
     password1=forms.CharField(label="Contraseña",max_length=50,required=True,widget=forms.PasswordInput)
     password2=forms.CharField(label="Confirmar Contraseña",required=True,widget=forms.PasswordInput)
     nombre=forms.CharField(label="Nombre",max_length=20,required=True)
     apellido=forms.CharField(label="Nombre",max_length=40,required=True)
     
     class Meta:
         model=User
         fields=['username','email','password1','password2','nombre','apellido']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)