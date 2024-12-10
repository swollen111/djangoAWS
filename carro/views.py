from django.shortcuts import render

from .carro import Carro

from tienda.models import Producto

from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("Tienda")


def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Tienda")


def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("Tienda")


def limpiar_carro(request, producto_id):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("Tienda")

# Este archivo define las vistas relacionadas con el manejo del carro de compras en la tienda.

# 1. `from django.shortcuts import render`:
#    - Importa la función `render`, que se usa para devolver una respuesta HTTP con una plantilla renderizada.
#    - Aunque en este archivo no se utiliza, generalmente se emplea para mostrar páginas HTML en Django.

# 2. `from .carro import Carro`:
#    - Importa la clase `Carro` del archivo `carro.py` (en el mismo directorio).
#    - `Carro` es una clase que probablemente maneja las operaciones del carrito de compras, como agregar, eliminar, o limpiar productos.

# 3. `from tienda.models import Producto`:
#    - Importa el modelo `Producto` desde la aplicación `tienda`.
#    - `Producto` es un modelo que representa los productos disponibles para compra en la tienda.

# 4. `from django.shortcuts import redirect`:
#    - Importa la función `redirect`, que se utiliza para redirigir al usuario a una URL diferente después de realizar alguna acción, como agregar un producto al carrito.

# 5. `agregar_producto(request, producto_id)`:
#    - Define una vista que maneja la acción de agregar un producto al carrito.
#    - Recibe el `producto_id` como argumento, que es el ID del producto a agregar.
#    - Se crea un objeto `Carro` basado en la sesión del usuario y se obtiene el producto usando el `producto_id`. Luego, se llama al método `agregar` de la clase `Carro` para añadir el producto al carrito.
#    - Después de agregar el producto, se redirige al usuario de vuelta a la página de la tienda.

# 6. `eliminar_producto(request, producto_id)`:
#    - Define una vista que maneja la acción de eliminar un producto del carrito.
#    - Similar a `agregar_producto`, recibe el `producto_id`, obtiene el producto, y llama al método `eliminar` de la clase `Carro` para remover el producto del carrito.
#    - Luego, redirige al usuario a la tienda.

# 7. `restar_producto(request, producto_id)`:
#    - Define una vista que permite restar la cantidad de un producto en el carrito.
#    - Al igual que las otras vistas, recibe el `producto_id`, obtiene el producto y llama al método `restar_producto` de la clase `Carro` para reducir la cantidad de ese producto en el carrito.
#    - Después, redirige al usuario a la tienda.

# 8. `limpiar_carro(request)`:
#    - Define una vista que limpia todo el contenido del carrito de compras.
#    - Llama al método `limpiar_carro` de la clase `Carro`, lo que elimina todos los productos del carrito.
#    - Finalmente, redirige al usuario a la tienda.

# En resumen, este archivo define las vistas que permiten a los usuarios agregar, eliminar, restar productos y limpiar su carrito de compras,
# interactuando con la clase `Carro` y el modelo `Producto`. Al final de cada acción, el usuario es redirigido a la página de la tienda.



