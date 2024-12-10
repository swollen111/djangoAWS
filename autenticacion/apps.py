from django.apps import AppConfig


class AutenticacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autenticacion'

# Este archivo configura la aplicación Django llamada "autenticacion".

# 1. `class AutenticacionConfig(AppConfig)`:
#    - Define la configuración para la aplicación "autenticacion".
#    - Hereda de la clase base `AppConfig` de Django.

# 2. `default_auto_field = 'django.db.models.BigAutoField'`:
#    - Especifica que el campo predeterminado para claves primarias en los modelos de esta aplicación será `BigAutoField`.

# 3. `name = 'autenticacion'`:
#    - Establece el nombre de la aplicación como "autenticacion".
#    - Este nombre se utiliza para registrar y referenciar la aplicación dentro del proyecto.

# En resumen, este archivo configura los ajustes básicos de la aplicación "autenticacion" dentro del proyecto Django.

