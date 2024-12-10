from django.contrib import admin

from .models import Pedido, LineaPedido

# Register your models here.

admin.site.register([Pedido, LineaPedido])

# Este archivo registra los modelos 'Pedido' y 'LineaPedido' en el panel de administración de Django.

# 1. `from django.contrib import admin`: 
#    - Importa el módulo `admin` de Django, que proporciona herramientas para administrar las aplicaciones del proyecto a través de una interfaz web.

# 2. `from .models import Pedido, LineaPedido`: 
#    - Importa los modelos `Pedido` y `LineaPedido` desde el archivo `models.py` de la misma aplicación. 
#    - Estos modelos representan las tablas de pedidos y líneas de pedido en la base de datos.

# 3. `admin.site.register([Pedido, LineaPedido])`: 
#    - Registra los modelos `Pedido` y `LineaPedido` en el sitio de administración de Django.
#    - Al registrar los modelos, Django crea automáticamente una interfaz de administración donde los administradores pueden agregar, editar y eliminar instancias de estos modelos en la base de datos.

# En resumen, este archivo registra los modelos 'Pedido' y 'LineaPedido' en el panel de administración de Django, permitiendo su gestión a través de la interfaz administrativa de Django.
