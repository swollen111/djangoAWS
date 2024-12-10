from django.urls import path

from .import views


urlpatterns = [
   
   
    path('',views.tienda, name="Tienda"),
   
    
]

# 1. `from django.urls import path`:
#    - Importa la función `path` de Django, que se utiliza para definir las rutas de URL en la aplicación.
#    - Cada ruta mapea una URL específica con una vista (función) que se ejecutará cuando un usuario acceda a esa URL.

# 2. `from .import views`:
#    - Importa las vistas (`views`) definidas en el archivo `views.py` de la misma aplicación.
#    - En este caso, importa la vista `tienda` que será utilizada en la ruta de la URL.

# 3. `urlpatterns = [`:
#    - Define una lista llamada `urlpatterns`, que contiene todas las rutas URL de la aplicación.
#    - Cada ruta es un mapeo entre una URL y una vista específica que manejará las solicitudes a esa URL.

# 4. `path('', views.tienda, name="Tienda")`:
#    - Define una ruta que corresponde a la URL raíz (`''`), es decir, cuando el usuario acceda a la página principal de la tienda.
#    - `views.tienda`: Especifica que la vista `tienda` (definida en el archivo `views.py`) debe ejecutarse cuando un usuario accede a esta URL.
#    - `name="Tienda"`: Asigna un nombre a esta ruta para que pueda ser referenciada de manera más fácil en otras partes del proyecto (como en las plantillas HTML o redirecciones).
   
# 5. `]`:
#    - Finaliza la lista `urlpatterns`, indicando que se han configurado todas las rutas URL para esta aplicación.

# En resumen, este archivo configura una URL en la aplicación de la tienda, que mapea la URL raíz (`''`) con la vista `tienda`, mostrando los productos disponibles cuando se accede a la página principal de la tienda.


