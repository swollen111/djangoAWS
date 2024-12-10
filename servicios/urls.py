from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
   
    path('',views.servicios, name="Servicios"),
    
    
]

# 1. `from django.urls import path`: 
#    - Importa la función `path` que se utiliza para definir las rutas de las URL en Django.

# 2. `from . import views`: 
#    - Importa las vistas definidas en el archivo `views.py` de la aplicación actual. En este caso, importa la vista `servicios`.

# 3. `from django.conf import settings`: 
#    - Importa la configuración de Django, que es donde se almacenan las variables de configuración del proyecto, como los directorios de archivos estáticos.

# 4. `from django.conf.urls.static import static`: 
#    - Importa la función `static` para servir archivos estáticos en desarrollo (como imágenes, CSS, JavaScript).

# 5. `urlpatterns = [ ... ]`: 
#    - Define las rutas de URL de la aplicación en una lista. Cada elemento de la lista es una ruta que asocia una URL con una vista.

# 6. `path('', views.servicios, name="Servicios")`: 
#    - Define una ruta para la URL raíz (`''`), es decir, la página principal de esta aplicación. 
#    - La vista asociada a esta URL es `servicios`, que está definida en `views.py`.
#    - `name="Servicios"` asigna un nombre a esta ruta para poder referirse a ella de manera más sencilla en otras partes del proyecto, como en las plantillas HTML.

# 7. `# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`: 
#    - Esta parte de código se usa para servir archivos estáticos (como imágenes o archivos de medios) cuando se ejecuta el servidor en modo desarrollo. 
#    - Este código está comentado en el fragmento, pero si estuviera habilitado, Django buscaría archivos en los directorios configurados en `MEDIA_URL` y `MEDIA_ROOT` de los ajustes.

# En resumen, este archivo de configuración de URL asocia la vista `servicios` a la URL raíz de la aplicación y permite el acceso a archivos estáticos en el desarrollo.


