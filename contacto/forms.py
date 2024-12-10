from django import forms

class FormularioContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", required=True)
    
    email=forms.CharField(label="Email", required=True)

    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)

# Este archivo define el formulario de contacto para la aplicación Django.

# 1. `from django import forms`:
#    - Importa el módulo `forms` de Django, que proporciona clases y herramientas para crear y manejar formularios.

# 2. `class FormularioContacto(forms.Form):`:
#    - Define una clase llamada `FormularioContacto`, que hereda de `forms.Form`. 
#    - Esta clase representa el formulario que se utilizará para capturar datos en la vista de contacto.

# 3. `nombre=forms.CharField(label="Nombre", required=True)`:
#    - Define un campo de formulario llamado `nombre`, que es un campo de texto (CharField).
#    - `label="Nombre"` establece el texto que se mostrará junto al campo en el formulario.
#    - `required=True` indica que este campo es obligatorio, es decir, el usuario no podrá enviarlo en blanco.

# 4. `email=forms.CharField(label="Email", required=True)`:
#    - Define un campo de formulario llamado `email`, que también es un campo de texto.
#    - Similar al campo `nombre`, se requiere que el usuario ingrese su dirección de correo electrónico.

# 5. `contenido=forms.CharField(label="Contenido", widget=forms.Textarea)`:
#    - Define un campo de formulario llamado `contenido`, que también es un campo de texto, pero con un widget especial de tipo `Textarea`.
#    - `Textarea` permite que el usuario ingrese texto en varias líneas, lo que es útil para campos como mensajes o descripciones.

# En resumen, este archivo crea un formulario con tres campos: nombre, email y contenido, que serán usados para capturar los datos del usuario en la vista de contacto.
