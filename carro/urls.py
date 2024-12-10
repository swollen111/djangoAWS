from django.urls import path

from .import views

app_name="carro"

urlpatterns = [
   
   
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
   
    
]

# Este archivo define las rutas de URL para las operaciones relacionadas con el carrito de compras.

# 1. `from django.urls import path`:
#    - Importa la función `path`, que se utiliza para definir las rutas de las URLs en Django.
#    - Cada ruta se asocia con una vista que se ejecutará cuando un usuario acceda a esa URL.

# 2. `from .import views`:
#    - Importa las vistas que están definidas en el archivo `views.py` de la misma aplicación.
#    - Estas vistas manejarán las operaciones cuando los usuarios interactúan con el carrito de compras.

# 3. `app_name="carro"`:
#    - Define el nombre del espacio de nombres para las URLs de esta aplicación, que en este caso es "carro".
#    - Esto permite un manejo más organizado y fácil de las URLs dentro del proyecto, especialmente cuando hay aplicaciones con rutas similares.

# 4. `urlpatterns`:
#    - Es una lista que define todas las rutas disponibles para la aplicación "carro".
#    - Cada ruta está asociada con una vista que maneja la lógica para esa acción del carrito.

# 5. `path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar")`:
#    - Define la ruta para agregar un producto al carrito.
#    - La URL contiene un parámetro dinámico `producto_id` que será utilizado para identificar el producto que el usuario quiere agregar.
#    - La vista `agregar_producto` se encargará de agregar el producto al carrito.
#    - El nombre de esta URL es `agregar`, lo que permite referirse a ella en las plantillas o en el código.

# 6. `path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar")`:
#    - Define la ruta para eliminar un producto del carrito.
#    - La URL contiene el parámetro `producto_id` para identificar qué producto eliminar.
#    - La vista `eliminar_producto` manejará la eliminación del producto del carrito.
#    - El nombre de esta URL es `eliminar`.

# 7. `path("restar/<int:producto_id>/", views.restar_producto, name="restar")`:
#    - Define la ruta para restar la cantidad de un producto en el carrito.
#    - Similar a las otras, la URL incluye el `producto_id` que especifica qué producto se quiere reducir en cantidad.
#    - La vista `restar_producto` se encargará de restar la cantidad del producto.
#    - El nombre de esta URL es `restar`.

# 8. `path("limpiar/", views.limpiar_carro, name="limpiar")`:
#    - Define la ruta para limpiar todo el carrito de compras.
#    - No incluye parámetros dinámicos, ya que esta acción afectará a todos los productos del carrito.
#    - La vista `limpiar_carro` vaciará el carrito completamente.
#    - El nombre de esta URL es `limpiar`.

# En resumen, este archivo `urls.py` configura las rutas necesarias para gestionar las acciones del carrito de compras, como agregar, eliminar, restar productos y limpiar el carrito.



