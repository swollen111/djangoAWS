from django.apps import AppConfig


class ServiciosConfig(AppConfig):
    name = 'servicios'

# 1. `from django.apps import AppConfig`:
#    - Importa la clase `AppConfig` de Django, que se utiliza para configurar aplicaciones dentro de un proyecto Django.
#    - Es parte de la configuración del proyecto, permitiendo a Django conocer y gestionar las aplicaciones de forma organizada.

# 2. `class ServiciosConfig(AppConfig):`:
#    - Define una clase llamada `ServiciosConfig`, que hereda de `AppConfig`. 
#    - Esta clase configura la aplicación llamada `servicios` dentro del proyecto Django.

# 3. `name = 'servicios'`:
#    - Especifica el nombre de la aplicación como 'servicios'. 
#    - Este nombre es utilizado por Django para identificar y gestionar esta aplicación en el proyecto.

# En resumen, esta clase configura la aplicación "servicios", permitiendo que Django la registre y administre correctamente dentro del proyecto.
