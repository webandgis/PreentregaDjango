from django import forms

class PortafolioForm(forms.Form):
    nombre=forms.CharField(max_length=50,required=True)
    lenguaje=forms.CharField(max_length=50,required=True)
    descripcion=forms.CharField(max_length=100,required=True)

class ContactoForm(forms.Form):
    nombre=forms.CharField(max_length=50,required=True)
    email=forms.EmailField(required=True)
    telefono=forms.IntegerField(required=True)
    mensaje=forms.CharField(max_length=100,required=True)
    
class ExperienciaForm(forms.Form):
    cargo=forms.CharField(max_length=50)
    institucion=forms.CharField(max_length=50)
    fechaDeInicio=forms.DateField()
    fechaDeEgreso=forms.DateField()
    descripcion=forms.CharField(max_length=100)
    contacto=forms.CharField(max_length=50)
    email=forms.EmailField()