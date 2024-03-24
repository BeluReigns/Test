from django.urls import path
from ReignsApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # URLs ÚNICOS
    path("", inicio, name="Home"),
    path("login/", iniciar_sesion, name="Iniciar Sesión"),
    path("logout/", cerrar_sesion, name="Cerrar Sesión"),
    path("singup/", registrarse, name="Registrarse"),
    path("edit/", editar_usuario, name="Editar Usuario"),
    path("ver_categorias/", ver_categorias, name="Ver Categorias"),
    path("contra/", CambiarContra.as_view(), name="Cambiar Contra"),
    path("avatar/", agregar_avatar, name="Nuevo Avatar"),

    #path("crear_calzado/", agregar_calzado, name="Crear calzado"),
    #path("leer_calzado/", ver_calzado, name="Ver calzado"),
    #path("editar_calzado/", actualizar_calzado, name="Editar calzado"),
    #path("eliminar_calzado", eliminar_calzado, name="Eliminar calzado"),

    # URLs CRUD con class CALZADO
    path("lista_calzado/", ListaCalzado.as_view(), name="CalzadosLeer"),
    path("crear_calzado/", CrearCalzado.as_view(), name="CalzadosCrear"),
    path("editar_calzado/<int:pk>", EditarCalzado.as_view(), name="CalzadosEditar"),
    path("eliminar_calzado/<int:pk>", EliminarCalzado.as_view(), name="CalzadosEliminar"),
    # URLs búsqueda y resultados
    path("buscar_calzado/", buscar_calzado, name="Buscar Calzado"),
    path("resultados_calzado/", resultado_calzado, name="Resultados Calzado"),

    # URLs CRUD con class ROPA
    path("lista_ropa/", ListaRopa.as_view(), name="RopaLeer"),
    path("crear_ropa/", CrearRopa.as_view(), name="RopaCrear"),
    path("editar_ropa/<int:pk>", EditarRopa.as_view(), name="RopaEditar"),
    path("eliminar_ropa/<int:pk>", EliminarRopa.as_view(), name="RopaEliminar"),
    # URLs búsqueda y resultados
    path("buscar_ropa/", buscar_ropa, name="Buscar en Ropa"),
    path("resultados_ropa/", resultado_ropa, name="Resultado Ropa"),

    # URLs CRUD con class LIBROS
    path("lista_libro/", ListaLibros.as_view(), name="LibroLeer"),
    path("crear_libro/", CrearLibros.as_view(), name="LibroCrear"),
    path("editar_libro/<int:pk>", EditarLibros.as_view(), name="LibroEditar"),
    path("eliminar_libro/<int:pk>", EliminarLibros.as_view(), name="LibroEliminar"),
    # URLs búsqueda y resultados
    path("buscar_libro/", buscar_libro, name="Buscar Libro"),
    path("resultados_libro/", resultado_libro, name="Resultado Libro"),

    # URLs CRUD con class MASCOTA
    path("lista_mascota/", ListaMascota.as_view(), name="MascotaLeer"),
    path("crear_mascota/", CrearMascota.as_view(), name="MascotaCrear"),
    path("editar_mascota/<int:pk>", EditarMascota.as_view(), name="MascotaEditar"),
    path("eliminar_mascota/<int:pk>", EliminarMascota.as_view(), name="MascotaEliminar"),
    # URLs búsqueda y resultados
    path("buscar_mascota/", buscar_mascota, name="Buscar Mascota"),
    path("resultados_mascota/", resultado_mascota, name="Resultado Mascota"),

    # URLs CRUD con class MISCELÁNEO
    path("lista_miscelaneo/", ListaMiscelaneo.as_view(), name="MiscelaneoLeer"),
    path("crear_miscelaneo/", CrearMiscelaneo.as_view(), name="MiscelaneoCrear"),
    path("editar_miscelaneo/<int:pk>", EditarMiscelaneo.as_view(), name="MiscelaneoEditar"),
    path("eliminar_miscelaneo/<int:pk>", EliminarMiscelaneo.as_view(), name="MiscelaneoEliminar"),
    # URLs búsqueda y resultados
    path("buscar_miscelaneo/", buscar_miscelaneo, name="Buscar Miscelaneo"),
    path("resultados_miscelaneo/", resultado_miscelaneo, name="Resultado Miscelaneo")
    
]