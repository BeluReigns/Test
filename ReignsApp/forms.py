from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
#from ReignsApp.models import Perfil

class RopaFormulario(forms.Form):
    prenda = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    talla = forms.CharField(max_length=10)
    precio = forms.IntegerField()

class CalzadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    talla = forms.CharField(max_length=10)
    precio = forms.IntegerField()
    
class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class LibrosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=20)
    precio = forms.IntegerField()

class MiscelaneoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=30)
    color = forms.CharField(max_length=20)
    talla = forms.CharField(max_length=10)
    precio = forms.IntegerField()

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()

class RegistroUsuario(UserCreationForm): # Para crear un formulario llamado RegistroUsuario

    class Meta: # Sirve para agregar o quitar campos dentro del formulario ya predefinido
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
  
class EditarUsuarioFormulario(UserChangeForm):
    
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')