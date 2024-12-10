from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

# Este archivo configura la aplicación Django llamada "blog".

# 1. `class BlogConfig(AppConfig)`:
#    - Define la configuración de la aplicación "blog".
#    - Hereda de la clase base `AppConfig` de Django, que se utiliza para registrar y configurar aplicaciones dentro de un proyecto Django.

# 2. `name = 'blog'`:
#    - Especifica el nombre de la aplicación como 'blog'. Este nombre es utilizado por Django para identificar y gestionar la aplicación dentro del proyecto.

# En resumen, este archivo es necesario para que Django reconozca y maneje la aplicación "blog" en el proyecto, permitiendo su correcto registro y funcionamiento.
