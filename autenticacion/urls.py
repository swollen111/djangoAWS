from django.urls import path

from .views import VRegistro, cerrar_sesion, logear



urlpatterns = [
   
  
    path('',VRegistro.as_view(), name="Autenticacion"),

    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),

    path('logear',logear, name="logear"),

    
]

# Este archivo define las rutas (URLs) asociadas a las vistas de autenticación de usuarios en la aplicación Django.

# 1. `path('', VRegistro.as_view(), name="Autenticacion")`:
#    - Asocia la vista de registro de usuarios (`VRegistro`) a la URL base del módulo.
#    - La vista se accede mediante su nombre `Autenticacion`.

# 2. `path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion")`:
#    - Asocia la función `cerrar_sesion` a la URL `/cerrar_sesion`.
#    - Permite cerrar la sesión activa del usuario.
#    - La vista se accede mediante su nombre `cerrar_sesion`.

# 3. `path('logear', logear, name="logear")`:
#    - Asocia la función `logear` a la URL `/logear`.
#    - Permite que los usuarios inicien sesión en la aplicación.
#    - La vista se accede mediante su nombre `logear`.

# En resumen, este archivo configura las rutas para gestionar el registro, inicio y cierre de sesión de usuarios en la aplicación.


