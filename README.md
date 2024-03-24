Django

La versión utilizada en este programa es la: 5.0.2
Si tiene una anterior, instalar o actualizar Django a versión necesaria Linux/Mac: python -m pip install Django==5.0.3 Windows: py -m pip install Django==5.0.3
Con el proyecto abierto en VSC u otro:

Hacer el paso previo para poder hacer la migración: python manage.py makemigrations
Luego hacer la migración: python manage.py migrate Una vez tengamos las migraciones podemos correr el servidor: python manage.py runserver Con el servidor corriendo podemos hacer uso/pruebas del programa de forma local.
URLs de uso local.

URLs de uso local:
http://127.0.0.1:8000/ReignsApp/ - Para ir al home de la web. Aquí puede empezar a navegar con los distintos botones.

CATEGORIAS
http://127.0.0.1:8000/ReignsApp/ver_categorias/ - Puede ir a una página dónde aparecen todas haciendo roll hacia abajo
- O a cada una por separado desde el navbar
  http://127.0.0.1:8000/ReignsApp/lista_ropa/
  http://127.0.0.1:8000/ReignsApp/lista_calzado/
  http://127.0.0.1:8000/ReignsApp/lista_mascota/
  http://127.0.0.1:8000/ReignsApp/lista_libro/
  http://127.0.0.1:8000/ReignsApp/lista_miscelaneo/
- En cada una de ellas se encuentra el botón para buscar en esa misma lista algún artículo en específico
  http://127.0.0.1:8000/ReignsApp/buscar_ropa/
  http://127.0.0.1:8000/ReignsApp/buscar_calzado/
  http://127.0.0.1:8000/ReignsApp/buscar_mascota/
  http://127.0.0.1:8000/ReignsApp/buscar_libro/
  http://127.0.0.1:8000/ReignsApp/buscar_miscelaneo/

REGISTRO
http://127.0.0.1:8000/ReignsApp/singup/ - para crear un usuario. Al iniciar sesión podrá crear, editar y eliminar productos

INICIAR SESIÓN
http://127.0.0.1:8000/ReignsApp/login/ - Al visitar las listas de cada categoría, al estar con sesión iniciada podrá ver el botón para crear artículo de cada categoría. Y cada artículo podrá editarlo o eliminarlo.

AVATAR
Al estar su sesión iniciada, en el navbar podrá ver el saludo con su nombre. Desde ahí podrá crear su avatar, subiendo la foto que Ud. desee. 

NAVBAR
Al lado derecho del navbar, podrá Editar su usuario, cambiár la contraseña y cerrar sesión, además de navegar por todas las categorías y sus contenidos.

Después de cerrar sesión, ya puede detener el servidor con control + c.