from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from carro.carro import Carro

from pedidos.models import LineaPedido, Pedido

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

from .models import Producto


# Create your views here.


@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user) # damos de alta un pedido
    carro=Carro(request)  # cogemos el carro
    lineas_pedido=list()  # lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items(): #recorremos el carro con sus items
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido                 
            ))

    LineaPedido.objects.bulk_create(lineas_pedido) # crea registros en BBDD en paquete
    #enviamos mail al cliente
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        

    )
    #mensaje para el futuro
    messages.success(request, "El pedido se ha creado correctamente")
    
    return redirect('../tienda')
    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html",{"productos":productos})
    

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario") 
                       
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="av72003@gmail.com"
    #to=kwargs.get("email_usuario")
    to="aquí la dirección del destinatario"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)

# Este archivo contiene las vistas que gestionan los pedidos y el procesamiento de estos en la tienda online. 

# 1. `from django.contrib import messages`:
#    - Importa el módulo `messages`, que permite enviar mensajes al usuario (por ejemplo, confirmaciones de acciones).

# 2. `from django.shortcuts import redirect, render`:
#    - Importa las funciones `redirect` (para redirigir al usuario a otra URL) y `render` (para renderizar plantillas HTML con un contexto).

# 3. `from django.contrib.auth.decorators import login_required`:
#    - Importa el decorador `login_required`, que asegura que el usuario esté autenticado antes de acceder a ciertas vistas.

# 4. `from carro.carro import Carro`:
#    - Importa la clase `Carro`, que gestiona el carrito de compras, permitiendo agregar, eliminar y manipular productos en el mismo.

# 5. `from pedidos.models import LineaPedido, Pedido`:
#    - Importa los modelos `LineaPedido` y `Pedido` desde la aplicación `pedidos`, que se utilizan para crear y almacenar la información del pedido realizado.

# 6. `from django.template.loader import render_to_string`:
#    - Importa la función `render_to_string`, que permite renderizar una plantilla HTML como una cadena de texto, útil para enviar correos electrónicos.

# 7. `from django.utils.html import strip_tags`:
#    - Importa la función `strip_tags`, que elimina las etiquetas HTML de un texto, útil cuando se quiere enviar un correo en formato texto plano.

# 8. `from django.core.mail import send_mail`:
#    - Importa la función `send_mail`, que se utiliza para enviar correos electrónicos desde Django.

# 9. `@login_required(login_url='/autenticacion/logear')`:
#    - Aplica el decorador `login_required` a la vista `procesar_pedido`, lo que significa que solo los usuarios autenticados pueden acceder a esta vista.
#    - Si el usuario no está autenticado, se le redirige a la página de login.

# 10. `def procesar_pedido(request):`:
#    - Esta vista crea un pedido y sus líneas correspondientes en función de los productos en el carrito del usuario.
#    - Se crean objetos `Pedido` y `LineaPedido` en la base de datos para almacenar la información del pedido.
#    - También se envía un correo de confirmación al usuario con los detalles del pedido.

# 11. `pedido=Pedido.objects.create(user=request.user)`:
#    - Crea un nuevo objeto `Pedido` con el usuario actual.

# 12. `carro=Carro(request)`:
#    - Crea una instancia del carrito de compras utilizando la clase `Carro`, que gestiona los productos del carrito en la sesión del usuario.

# 13. `for key, value in carro.carro.items():`:
#    - Recorre los elementos del carrito para crear las líneas de pedido correspondientes a los productos en el carrito.

# 14. `LineaPedido.objects.bulk_create(lineas_pedido)`:
#    - Crea varias instancias de `LineaPedido` de manera eficiente en la base de datos utilizando el método `bulk_create`.

# 15. `enviar_mail(...)`:
#    - Llama a la función `enviar_mail` para enviar un correo electrónico al usuario con los detalles del pedido.

# 16. `messages.success(request, "El pedido se ha creado correctamente")`:
#    - Envía un mensaje de éxito al usuario indicando que el pedido se ha procesado correctamente.

# 17. `return redirect('../tienda')`:
#    - Redirige al usuario a la página principal de la tienda después de procesar el pedido.

# 18. `def enviar_mail(**kwargs):`:
#    - Esta función se encarga de enviar un correo electrónico al usuario con los detalles del pedido.
#    - Usa la plantilla `emails/pedido.html` para generar el contenido HTML del correo, y `strip_tags` para generar una versión en texto plano.

# 19. `send_mail(...)`:
#    - Envía el correo electrónico utilizando la función `send_mail` de Django, enviando tanto la versión en HTML como la versión en texto plano del correo.

# En resumen, este archivo gestiona la creación y el procesamiento de pedidos, incluyendo la creación de líneas de pedido en la base de datos y el envío de correos electrónicos de confirmación al usuario.

