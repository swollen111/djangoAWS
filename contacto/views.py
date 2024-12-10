from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage


# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")


            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["aquí la dirección del destinatario"],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})

# Este archivo define la vista para la página de contacto de tu aplicación Django. 
# Permite que los usuarios envíen un mensaje de contacto que se enviará por correo electrónico.

# 1. `from django.shortcuts import render, redirect`:
#    - Importa las funciones `render` y `redirect` de Django.
#    - `render` se usa para devolver una respuesta HTTP con una plantilla renderizada.
#    - `redirect` se utiliza para redirigir al usuario a una URL específica después de una acción, como el envío de un formulario.

# 2. `from .forms import FormularioContacto`:
#    - Importa el formulario `FormularioContacto` que se utiliza para validar y procesar los datos del contacto enviado por el usuario.

# 3. `from django.core.mail import EmailMessage`:
#    - Importa la clase `EmailMessage` de Django, que se utiliza para crear y enviar correos electrónicos.

# 4. `def contacto(request):`:
#    - Define la vista `contacto` que se encarga de gestionar las solicitudes GET y POST del formulario de contacto.
#    - Esta vista se llama cuando el usuario visita la página de contacto o envía el formulario de contacto.

# 5. `formulario_contacto = FormularioContacto()`:
#    - Crea una instancia del formulario `FormularioContacto` para que se pase a la plantilla al cargar la página inicialmente.

# 6. `if request.method == "POST":`:
#    - Comprueba si la solicitud es de tipo POST, lo que indica que el formulario ha sido enviado.
#    - Si es así, crea una instancia del formulario con los datos enviados por el usuario (`request.POST`).

# 7. `if formulario_contacto.is_valid():`:
#    - Verifica que el formulario enviado sea válido según las validaciones definidas en el formulario.

# 8. `nombre = request.POST.get("nombre")`, `email = request.POST.get("email")`, `contenido = request.POST.get("contenido")`:
#    - Obtiene los valores del formulario enviados por el usuario (nombre, correo electrónico y contenido del mensaje).

# 9. `email = EmailMessage(...)`:
#    - Crea un objeto `EmailMessage` con el asunto, el cuerpo del mensaje y las direcciones de correo (incluyendo la dirección de respuesta).

# 10. `try: email.send()`:
#    - Intenta enviar el correo electrónico usando el método `send()` de la clase `EmailMessage`.
#    - Si el correo se envía con éxito, redirige al usuario a la página de contacto con un mensaje de éxito (`/contacto/?valido`).
#    - Si ocurre algún error al enviar el correo, redirige a la misma página con un mensaje de error (`/contacto/?novalido`).

# 11. `return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})`:
#    - Si el formulario no se envía, renderiza la plantilla `contacto.html` con el formulario para que el usuario pueda completarlo.

# En resumen, esta vista gestiona el formulario de contacto de la aplicación. Recibe los datos del formulario de contacto, valida la entrada del usuario, y si todo es válido, envía un correo electrónico al destinatario especificado. Luego, redirige al usuario a la página de contacto con un mensaje de éxito o error.
