from django.apps import AppConfig


class ContactoConfig(AppConfig):
    name = 'contacto'

# Este archivo configura la aplicación "contacto" dentro del proyecto Django.

# 1. `from django.apps import AppConfig`:
#    - Importa la clase `AppConfig` de Django, que se utiliza para definir y configurar las aplicaciones dentro del proyecto.

# 2. `class ContactoConfig(AppConfig):`:
#    - Define una clase llamada `ContactoConfig`, que hereda de `AppConfig`.
#    - Esta clase se utiliza para configurar la aplicación "contacto" y proporcionar opciones personalizadas si es necesario.

# 3. `name = 'contacto'`:
#    - Asigna el nombre de la aplicación como `'contacto'`.
#    - Este es el nombre que Django utiliza internamente para identificar y gestionar la aplicación en el proyecto.

# En resumen, este archivo define y configura la aplicación "contacto", permitiendo que Django la registre correctamente en el proyecto y administre sus funcionalidades.
