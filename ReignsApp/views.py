from django.shortcuts import render, redirect
from ReignsApp.models import *
from ReignsApp.forms import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
# Iniciar Sesión
def iniciar_sesion(request):    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST) # Almacena la info que se ha puesto en el form
        if formulario.is_valid():
            info_dict = formulario.cleaned_data # Convierte la info del form a diccionario de python
            usuario = authenticate(username=info_dict["username"], password=info_dict["password"])
            if usuario is not None: # si el usuario no es nulo, o sea existe
                login(request, usuario) # Aquí te dice que tu cuenta está activa
                return render(request, "ReignsApp/inicio.html", {"mensaje":f"¡Bienvenido {usuario}!"})
        else: 
            return render(request, "ReignsApp/inicio.html", {"mensaje":"Error al iniciar la sesión"})
    else:
        formulario = AuthenticationForm()
    return render(request, "ReignsApp/registro/iniciar_sesion.html", {"formu":formulario})

# Registrarse
#def register(request):
#    if request.method == 'POST':
#        user_form = RegistroUsuario(request.POST)
#        if user_form.is_valid():
#            new_user = user_form.save(commit=False)
#            new_user.set_password(user_form.cleaned_data['password1'])
#            new_user.save()
#            return render(request, 'ReignsApp/registro_done.html', {'new_user': new_user})
#        else: 
#            return render(request, "ReignsApp/inicio.html", {"mensaje":"Error al iniciar la sesión"})
#    else:
#        user_form = RegistroUsuario()
#    return render(request, 'ReignsApp/registro.html', {'user_form': user_form})

# registrarse

def registrarse(request):
    if request.method == "POST":
        formulario = RegistroUsuario(request.POST)
        if formulario.is_valid():
            formulario.save() # Esto crea el nuevo usuario
            return render(request, "ReignsApp/registro/registro_done.html", {"mensaje":"El usuario ha sido creado"})
    else:
        formulario = RegistroUsuario()
    return render(request, "ReignsApp/registro/registro.html", {"formu":formulario})

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            usuario_actual = User.objects.get(username=request.user)
            nuevo_avatar = Avatar(usuario=usuario_actual, imagen=info["imagen"])
            nuevo_avatar.save()
            return render(request, "ReignsApp/inicio.html", {"mensaje":"Has creado tu avatar"})
    else:
        formulario = AvatarFormulario()
    return render(request, "ReignsApp/registro/nuevo_avatar.html", {"formu":formulario})

# logout
def cerrar_sesion(request):
    logout(request)
    return render(request, "ReignsApp/inicio.html", {"mensaje":"Se ha cerrado la sesión correctamente"})

# User edit
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        form = EditarUsuarioFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
#           usuario.set_password(info["password1"])
            usuario.save()
            return render(request, "ReignsApp/inicio.html")
    else:
        form = EditarUsuarioFormulario(initial={
                                "email":usuario.email,
                                "first_name":usuario.first_name,
                                "last_name":usuario.last_name
                                })
    
    return render(request, "ReignsApp/registro/editar_usuario.html", {"formu":form})

# página de inicio
def inicio(request):
    return render(request, "ReignsApp/inicio.html", {"mensaje":"Bienvenidos a este reinado disperso ^^"})

#@login_required - necesito estar con sesión iniciada para poder acceder a esta vista
def ver_categorias(request):
    return render(request, "ReignsApp/ver_categorias.html")

class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "ReignsApp/registro/cambiar_contra.html"
    success_url = "/ReignsApp/"

# CRUD + búsqueda y resultados Calzado
class ListaCalzado(ListView):
    model = Calzado
    template_name = "ReignsApp/Calzado/lista_calzado.html"
    fields = ["id","nombre","marca","color","talla","precio"]

class CrearCalzado(LoginRequiredMixin, CreateView):
    model = Calzado
    template_name = "ReignsApp/Calzado/crear_calzado.html"
    fields = ["nombre","marca","color","talla","precio"]
    success_url = "/ReignsApp/buscar_calzado/"

class EditarCalzado(LoginRequiredMixin, UpdateView):
    model = Calzado
    template_name = "ReignsApp/Calzado/editar_calzado.html"
    fields = ["nombre","marca","color","talla","precio"]
    success_url = "/ReignsApp/lista_calzado/"

class EliminarCalzado(LoginRequiredMixin, DeleteView):
    model = Calzado
    template_name = "ReignsApp/Calzado/eliminar_calzado.html"
    success_url = "/ReignsApp/"

def buscar_calzado(request):
    return render(request, "ReignsApp/Calzado/buscar_calzado.html")

def resultado_calzado(request):
    calzado = request.GET["calzado"]    
    resultados = Calzado.objects.filter(nombre__iexact=calzado)    
    return render(request, "ReignsApp/Calzado/resultados_calzado.html", {"form":resultados})

# CRUD + búsqueda y resultados Ropa
class ListaRopa(ListView):
    model = Ropa
    template_name = "ReignsApp/Ropa/lista_ropa.html"
    fields = ["id","prenda","marca","color","talla","precio"]

class CrearRopa(LoginRequiredMixin, CreateView):
    model = Ropa
    template_name = "ReignsApp/Ropa/crear_ropa.html"
    fields = ["prenda","marca","color","talla","precio"]
    success_url = "/ReignsApp/buscar_ropa/"

class EditarRopa(LoginRequiredMixin, UpdateView):
    model = Ropa
    template_name = "ReignsApp/Ropa/editar_ropa.html"
    fields = ["prenda","marca","color","talla","precio"]
    success_url = "/ReignsApp/lista_ropa/"

class EliminarRopa(LoginRequiredMixin, DeleteView):
    model = Ropa
    template_name = "ReignsApp/Ropa/eliminar_ropa.html"
    success_url = "/ReignsApp/"

def buscar_ropa(request):
    return render(request, "ReignsApp/Ropa/buscar_ropa.html")

def resultado_ropa(request):
    ropa = request.GET["ropa"]    
    resultados = Ropa.objects.filter(prenda=ropa)    
    return render(request, "ReignsApp/Ropa/resultados_ropa.html", {"form":resultados})

# CRUD + búsqueda y resultados Libros
class ListaLibros(ListView):
    model = Libros
    template_name = "ReignsApp/Libro/lista_libro.html"
    fields = ["id","nombre","autor","precio"]

class CrearLibros(LoginRequiredMixin, CreateView):
    model = Libros
    template_name = "ReignsApp/Libro/crear_libro.html"
    fields = ["nombre","autor","precio"]
    success_url = "/ReignsApp/buscar_libro/"

class EditarLibros(LoginRequiredMixin, UpdateView):
    model = Libros
    template_name = "ReignsApp/Libro/editar_libro.html"
    fields = ["nombre","autor","precio"]
    success_url = "/ReignsApp/lista_libro/"

class EliminarLibros(LoginRequiredMixin, DeleteView):
    model = Libros
    template_name = "ReignsApp/Libro/eliminar_libro.html"
    success_url = "/ReignsApp/"

def buscar_libro(request):
    return render(request, "ReignsApp/Libro/buscar_libro.html")

def resultado_libro(request):
    libro = request.GET["libro"]    
    resultados = Libros.objects.filter(nombre__iexact=libro)    
    return render(request, "ReignsApp/Libro/resultados_libro.html", {"form":resultados})

# CRUD + búsqueda y resultados Mascota
class ListaMascota(ListView):
    model = Mascota
    template_name = "ReignsApp/Mascota/lista_mascota.html"
    fields = ["id","nombre","descripcion","precio"]

class CrearMascota(LoginRequiredMixin, CreateView):
    model = Mascota
    template_name = "ReignsApp/Mascota/crear_mascota.html"
    fields = ["nombre","descripcion","precio"]
    success_url = "/ReignsApp/buscar_mascota/"

class EditarMascota(LoginRequiredMixin, UpdateView):
    model = Mascota
    template_name = "ReignsApp/Mascota/editar_mascota.html"
    fields = ["nombre","descripcion","precio"]
    success_url = "/ReignsApp/lista_mascota/"

class EliminarMascota(LoginRequiredMixin, DeleteView):
    model = Mascota
    template_name = "ReignsApp/Mascota/eliminar_mascota.html"
    success_url = "/ReignsApp/"

def buscar_mascota(request):
    return render(request, "ReignsApp/Mascota/buscar_mascota.html")

def resultado_mascota(request):
    mascota = request.GET["mascota"]    
    resultados = Mascota.objects.filter(nombre__iexact=mascota)    
    return render(request, "ReignsApp/Mascota/resultados_mascota.html", {"form":resultados})

# CRUD + búsqueda y resultados Miscelaneo
class ListaMiscelaneo(ListView):
    model = Miscelaneo
    template_name = "ReignsApp/Miscelaneo/lista_Miscelaneo.html"
    fields = ["id","nombre","descripcion","color","talla","precio"]

class CrearMiscelaneo(LoginRequiredMixin, CreateView):
    model = Miscelaneo
    template_name = "ReignsApp/Miscelaneo/crear_miscelaneo.html"
    fields = ["nombre","descripcion","color","talla","precio"]
    success_url = "/ReignsApp/buscar_miscelaneo/"

class EditarMiscelaneo(LoginRequiredMixin, UpdateView):
    model = Miscelaneo
    template_name = "ReignsApp/Miscelaneo/editar_miscelaneo.html"
    fields = ["nombre","descripcion","color","talla","precio"]
    success_url = "/ReignsApp/lista_miscelaneo/"

class EliminarMiscelaneo(LoginRequiredMixin, DeleteView):
    model = Miscelaneo
    template_name = "ReignsApp/Miscelaneo/eliminar_miscelaneo.html"
    success_url = "/ReignsApp/"

def buscar_miscelaneo(request):
    return render(request, "ReignsApp/Miscelaneo/buscar_miscelaneo.html")

def resultado_miscelaneo(request):
    miscelaneo = request.GET["miscelaneo"]    
    resultados = Miscelaneo.objects.filter(nombre__iexact=miscelaneo)    
    return render(request, "ReignsApp/Miscelaneo/resultados_miscelaneo.html", {"form":resultados})