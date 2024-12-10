from django.urls import path

from . import views



urlpatterns = [
   
  
    path('',views.contacto, name="Contacto"),
    
]

# Este archivo define las rutas (URLs) para la vista de contacto de la aplicación Django.

# 1. `from django.urls import path`:
#    - Importa la función `path` de Django, que se utiliza para definir las rutas en el archivo `urls.py` de la aplicación.

# 2. `from . import views`:
#    - Importa las vistas (funciones) definidas en el archivo `views.py` de la misma aplicación. 
#    - En este caso, se importa la vista `contacto` que se utilizará en la ruta.

# 3. `urlpatterns = [...]`:
#    - La lista `urlpatterns` contiene las rutas de la aplicación. 
#    - Cada ruta está asociada con una vista específica, que maneja las solicitudes a esa ruta.

# 4. `path('', views.contacto, name="Contacto")`:
#    - Define una ruta para la página principal de contacto de la aplicación.
#    - `''` es la ruta base de la aplicación (es decir, la URL `/contacto/`).
#    - `views.contacto` es la vista que maneja las solicitudes a esta URL.
#    - `name="Contacto"` asigna un nombre a esta ruta, que se puede usar para hacer referencia a la URL en otras partes del proyecto.

# En resumen, este archivo define la URL para acceder al formulario de contacto, que está asociado con la vista `contacto` del archivo `views.py`.


