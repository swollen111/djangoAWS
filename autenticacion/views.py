from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request, usuario)

            return redirect('Home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"registro/registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)

    return redirect('Home')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "información incorrecta")

    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})

# Este código define vistas para gestionar el registro, inicio y cierre de sesión de usuarios en una aplicación Django.

# 1. La clase `VRegistro` implementa la vista de registro de usuarios:
#    - Método `get`: Muestra un formulario de registro vacío (basado en `UserCreationForm`).
#    - Método `post`: Procesa los datos enviados por el usuario. Si el formulario es válido:
#        * Guarda el nuevo usuario en la base de datos.
#        * Inicia la sesión automáticamente con `login()`.
#        * Redirige a la página principal ('Home').
#      Si el formulario contiene errores, los muestra al usuario y recarga el formulario.

# 2. La función `cerrar_sesion` cierra la sesión activa del usuario utilizando `logout()` y lo redirige a la página principal ('Home').

# 3. La función `logear` gestiona el inicio de sesión:
#    - Si se envía un formulario por POST:
#        * Valida los datos con `AuthenticationForm`.
#        * Autentica al usuario con `authenticate()` y, si es válido:
#            - Inicia la sesión con `login()`.
#            - Redirige a la página principal ('Home').
#        * Si los datos son incorrectos, muestra un mensaje de error.
#    - Si no es una petición POST, muestra un formulario vacío para iniciar sesión.

# En resumen, este archivo implementa las funcionalidades básicas de autenticación de usuarios en Django
# utilizando formularios proporcionados por `django.contrib.auth.forms`.



    

        
