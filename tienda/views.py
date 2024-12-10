from django.shortcuts import render


from .models import Producto




# Create your views here.


def tienda(request):    
    
    
    productos=Producto.objects.all()

    return render(request, "tienda/tienda.html", {"productos":productos})

# 1. `from django.shortcuts import render`:
#    - Importa la función `render` de Django, que se utiliza para renderizar una plantilla HTML y devolverla como respuesta HTTP.
#    - Esta función facilita la combinación de datos dinámicos con una plantilla para generar la respuesta final que se enviará al cliente.

# 2. `from .models import Producto`:
#    - Importa el modelo `Producto` desde el archivo `models.py` de la misma aplicación.
#    - Esto es necesario para interactuar con la base de datos y obtener los productos que se mostrarán en la tienda.

# 3. `def tienda(request):`:
#    - Define la vista `tienda`, que se ejecutará cuando el usuario acceda a la página de la tienda.
#    - Recibe el objeto `request` como argumento, que contiene la información de la solicitud HTTP.

# 4. `productos=Producto.objects.all()`:
#    - Recupera todos los objetos `Producto` desde la base de datos utilizando el ORM de Django.
#    - `Producto.objects.all()` devuelve una consulta que obtiene todos los productos disponibles en la base de datos.

# 5. `return render(request, "tienda/tienda.html", {"productos": productos})`:
#    - Utiliza la función `render` para devolver la respuesta HTTP con la plantilla `tienda.html`.
#    - Pasa el contexto `{"productos": productos}` a la plantilla, lo que permite que los productos obtenidos desde la base de datos estén disponibles para ser mostrados en la página HTML.
#    - La plantilla `tienda.html` será renderizada con la lista de productos proporcionada.

# En resumen, esta vista obtiene todos los productos desde la base de datos y los pasa a la plantilla `tienda.html` para que sean mostrados en la página de la tienda.
