from django.urls import path

from .import views



urlpatterns = [
   
   
    path("", views.procesar_pedido, name="procesar_pedido")
    
    
   
    
]

# Este archivo define las rutas de URL para la funcionalidad relacionada con los pedidos.

# 1. `from django.urls import path`: 
#    - Importa la función `path`, que se usa para definir las rutas de las URLs.

# 2. `from . import views`: 
#    - Importa las vistas de la aplicación actual para asociarlas con las rutas.

# 3. `urlpatterns = [...]`: 
#    - Una lista que contiene las rutas URL de la aplicación.

# 4. `path("", views.procesar_pedido, name="procesar_pedido")`: 
#    - Define la ruta para procesar un pedido cuando el usuario accede a la URL raíz de esta aplicación.
#    - `views.procesar_pedido`: Llama a la vista `procesar_pedido` cuando se accede a esta ruta.
#    - `name="procesar_pedido"`: Asocia un nombre a esta URL, lo que permite referenciarla fácilmente en otras partes del proyecto.

# En resumen, este archivo configura la ruta que procesa un pedido cuando el usuario llega a la URL definida en la aplicación.


