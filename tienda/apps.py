from django.apps import AppConfig


class TiendaConfig(AppConfig):
    name = 'tienda'

# 1. `from django.apps import AppConfig`:
#    - Importa la clase `AppConfig` desde el módulo `django.apps`, que se utiliza para configurar una aplicación en Django.
#    - `AppConfig` permite configurar propiedades específicas para la aplicación, como el nombre del módulo, las señales o la configuración de la base de datos.

# 2. `class TiendaConfig(AppConfig):`:
#    - Define una clase `TiendaConfig` que hereda de `AppConfig`.
#    - Esta clase configura la aplicación `tienda` dentro del proyecto Django.
#    - La clase se utiliza para inicializar y configurar cualquier aspecto de la aplicación `tienda` cuando Django arranca.

# 3. `name = 'tienda'`:
#    - Establece el nombre de la aplicación como `'tienda'`.
#    - Este nombre debe coincidir con el nombre del directorio de la aplicación y es utilizado por Django para reconocer e identificar la aplicación dentro del proyecto.
