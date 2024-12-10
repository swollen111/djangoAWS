from django.apps import AppConfig


class PedidosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pedidos'

# Este archivo configura la aplicación Django llamada 'pedidos'.

# 1. `from django.apps import AppConfig`: 
#    - Importa la clase base `AppConfig` de Django, que se utiliza para configurar y registrar aplicaciones dentro de un proyecto Django.

# 2. `class PedidosConfig(AppConfig)`: 
#    - Define una clase `PedidosConfig` que hereda de `AppConfig`. 
#    - Esta clase se utilizará para configurar la aplicación `pedidos`.

# 3. `default_auto_field = 'django.db.models.BigAutoField'`: 
#    - Establece que, por defecto, los campos `AutoField` generados para los modelos de esta aplicación utilizarán `BigAutoField`. 
#    - Esto es útil para proyectos que requieren IDs más grandes para sus registros. `BigAutoField` usa un entero de 64 bits en lugar del entero de 32 bits utilizado por defecto en `AutoField`.

# 4. `name = 'pedidos'`: 
#    - Especifica el nombre de la aplicación como `'pedidos'`.
#    - Django utiliza este nombre para reconocer y gestionar la aplicación dentro del proyecto.

# En resumen, este archivo configura la aplicación `pedidos` en el proyecto Django, asegurándose de que use el campo `BigAutoField` de forma predeterminada para los identificadores y se registre correctamente con su nombre.
