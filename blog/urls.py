from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
   
    path('',views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria")
    
    
]

# Este archivo define las rutas (URLs) relacionadas con las vistas del blog en la aplicación Django.

# 1. `path('', views.blog, name="Blog")`:
#    - Asocia la URL base del módulo (`''`) a la vista `blog` definida en `views.py`.
#    - La vista `blog` se utiliza para mostrar todas las publicaciones del blog.
#    - La ruta se accede mediante el nombre `Blog`.

# 2. `path('categoria/<int:categoria_id>/', views.categoria, name="categoria")`:
#    - Define una URL dinámica para mostrar las publicaciones de una categoría específica.
#    - `<int:categoria_id>` captura un valor entero de la URL y lo pasa como argumento a la vista `categoria`.
#    - La ruta se accede mediante el nombre `categoria`.

# 3. `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` (opcional si se añade más tarde):
#    - Si se utiliza, esta configuración permite servir archivos estáticos o multimedia durante el desarrollo.
#    - `MEDIA_URL` define la URL base para acceder a los archivos multimedia.
#    - `MEDIA_ROOT` define la ubicación física de los archivos multimedia.

# En resumen, este archivo configura las rutas necesarias para mostrar todas las publicaciones del blog
# y para filtrar publicaciones por categoría.
