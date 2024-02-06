from django.db import models

# Create your models here.
class Experiencia(models.Model):
    cargo=models.CharField(max_length=50)
    institucion=models.CharField(max_length=50)
    fechaDeInicio=models.DateField()
    fechaDeEgreso=models.DateField()
    descripcion=models.CharField(max_length=100)
    contacto=models.CharField(max_length=50)
    email=models.EmailField()
    
    
    
    def __str__(self):
         return f"{self.cargo},{self.institucion}"

class Portafolio(models.Model):
    nombre=models.CharField(max_length=50)
    lenguaje=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)

    def __str__(self):
         return f"{self.nombre}"
class Contacto(models.Model):
     nombre=models.CharField(max_length=50)
     email=models.EmailField()
     telefono=models.IntegerField(max_length=10)
     mensaje=models.CharField(max_length=100)
     
     def __str__(self):
      f"{self.nombre}"
     
    
        