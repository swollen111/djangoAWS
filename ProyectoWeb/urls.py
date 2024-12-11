"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('servicios/', include('servicios.urls')),

    path('blog/', include('blog.urls')),

    path('contacto/', include('contacto.urls')),

    path('autenticacion/', include('autenticacion.urls')),

    path('tienda/', include('tienda.urls')),  

    path('carro/', include('carro.urls')),  

    path('pedidos/', include('pedidos.urls')),  

    path('', include('ProyectoWebApp.urls')),

       
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Este archivo de configuración de URLs (`urls.py`) define las rutas (URLs) de todo el proyecto Django "ProyectoWeb".
# Las rutas permiten que las solicitudes HTTP sean dirigidas a las vistas correspondientes de cada aplicación dentro del proyecto.

# 1. **Importación de Módulos:**
#    - Se importan varias funciones y módulos de Django, como `path` para definir las rutas, `include` para incluir URLs de otras aplicaciones, y `static` para manejar archivos estáticos.
#    - `settings` y `static` se importan para servir los archivos estáticos y multimedia correctamente durante el desarrollo.

# 2. **Rutas Principales del Proyecto:**
#    - `admin/`: Ruta para acceder al panel de administración de Django (vista proporcionada por `admin.site.urls`).
#    - `servicios/`, `blog/`, `contacto/`, `autenticacion/`, `tienda/`, `carro/`, `pedidos/`: Rutas que incluyen las URLs de sus respectivas aplicaciones. Estas rutas dirigen las solicitudes a las vistas dentro de las aplicaciones `servicios`, `blog`, `contacto`, `autenticacion`, `tienda`, `carro` y `pedidos`.
#    - Cada una de estas rutas incluye el archivo `urls.py` correspondiente de la aplicación asociada, lo que permite modularizar las rutas y mejorar la estructura del proyecto.

# 3. **Ruta por Defecto:**
#    - `''`: Esta ruta corresponde a la página de inicio del proyecto y se redirige a las URLs definidas en `ProyectoWebApp.urls`. Esta es la ruta base cuando no se especifica una URL en particular.

# 4. **Archivos Estáticos y Multimedia:**
#    - Se usan las funciones `static` para servir archivos estáticos (CSS, JS, imágenes) y archivos multimedia (como imágenes subidas por los usuarios).
#    - `static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)` configura la ruta para servir archivos estáticos.
#    - `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` configura la ruta para servir archivos multimedia.

# En resumen, este archivo es el encargado de definir todas las rutas de acceso a las vistas y aplicaciones del proyecto, además de configurar cómo manejar los archivos estáticos y multimedia en el entorno de desarrollo.

