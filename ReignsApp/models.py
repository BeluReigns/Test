from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ropa(models.Model):
    prenda = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    talla = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return self.prenda

class Calzado(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    talla = models.CharField(max_length=10)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Libros(models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Miscelaneo(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    talla = models.CharField(max_length=10)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

#class Perfil(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    email = models.EmailField()
#    nombre = models.CharField(max_length=30)
#    apellido = models.CharField(max_length=30)
    
#    def __str__(self):
#        return self.user
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)