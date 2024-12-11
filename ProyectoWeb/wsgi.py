"""
WSGI config for ProyectoWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoWeb.settings')

application = get_wsgi_application()

# Este archivo es el punto de entrada para el servidor WSGI (Web Server Gateway Interface) del proyecto Django.
# El archivo `wsgi.py` es utilizado cuando el proyecto se despliega en un servidor de producción. 

# 1. **Importación de Módulos:**
#    - Se importa el módulo `os` para interactuar con el sistema operativo.
#    - `get_wsgi_application` se importa desde `django.core.wsgi` para obtener la aplicación WSGI de Django. Esta es la función que el servidor WSGI invocará para manejar las solicitudes HTTP.

# 2. **Configuración del Entorno de Django:**
#    - `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoWeb.settings')`: Esta línea configura la variable de entorno `DJANGO_SETTINGS_MODULE` para que apunte al archivo de configuración de ajustes del proyecto (`settings.py`). Esto es necesario para que Django sepa qué configuración utilizar en el entorno de producción.
  
# 3. **Creación de la Aplicación WSGI:**
#    - `application = get_wsgi_application()`: Esta línea obtiene la aplicación WSGI de Django y la asigna a la variable `application`. Este es el objeto que será utilizado por el servidor WSGI para manejar todas las solicitudes HTTP entrantes.

# En resumen, este archivo es crucial para la implementación del proyecto en servidores de producción. Proporciona un punto de entrada para el servidor web que interactúa con el proyecto Django y maneja las solicitudes HTTP utilizando el estándar WSGI.

