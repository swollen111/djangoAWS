from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})

# Este archivo define la vista para mostrar los servicios disponibles en la aplicación.

# 1. `from django.shortcuts import render`: 
#    - Importa la función `render` de Django, que se utiliza para renderizar una plantilla HTML y devolverla como respuesta al usuario.

# 2. `from servicios.models import Servicio`: 
#    - Importa el modelo `Servicio` desde el archivo `models.py` de la aplicación `servicios`. 
#    - Este modelo representa la tabla de servicios en la base de datos.

# 3. `def servicios(request):`:
#    - Define una vista llamada `servicios`, que maneja las solicitudes a la URL asociada.
#    - El parámetro `request` contiene la solicitud HTTP que el cliente hace al servidor.

# 4. `servicios = Servicio.objects.all()`:
#    - Recupera todos los objetos del modelo `Servicio` desde la base de datos.
#    - `objects.all()` es un método de Django que devuelve todos los registros de la tabla correspondiente al modelo.

# 5. `return render(request, "servicios/servicios.html", {"servicios": servicios})`:
#    - La función `render` genera una respuesta HTTP con el contenido de la plantilla `servicios.html`, ubicada en la carpeta `servicios`.
#    - La variable `servicios`, que contiene todos los objetos `Servicio`, se pasa al contexto de la plantilla, lo que permite acceder a los servicios desde la plantilla HTML.
#    - La plantilla `servicios.html` se renderiza con la información de los servicios y se devuelve al usuario.

# En resumen, esta vista consulta todos los servicios desde la base de datos y los pasa a una plantilla HTML para que se muestren en la página web.

