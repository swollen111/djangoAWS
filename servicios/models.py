from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="servicios")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo

# 1. `from django.db import models`:
#    - Importa el módulo `models` de Django, que contiene las herramientas para definir modelos y campos en la base de datos.

# 2. `class Servicio(models.Model):`:
#    - Define el modelo `Servicio`, que será utilizado para representar los servicios en la base de datos.
#    - Hereda de `models.Model`, lo que permite que Django cree una tabla en la base de datos con las columnas correspondientes.

# 3. `titulo = models.CharField(max_length=50)`:
#    - Define un campo de texto para almacenar el título del servicio. 
#    - El parámetro `max_length=50` establece que el título puede tener hasta 50 caracteres.

# 4. `contenido = models.CharField(max_length=50)`:
#    - Define un campo de texto para almacenar el contenido o descripción del servicio.
#    - Al igual que el campo `titulo`, tiene un `max_length=50`, que limita la longitud del texto.

# 5. `imagen = models.ImageField(upload_to="servicios")`:
#    - Define un campo para almacenar la imagen asociada al servicio.
#    - El parámetro `upload_to="servicios"` indica que las imágenes se almacenarán en una carpeta llamada "servicios" dentro del directorio de medios configurado en Django.

# 6. `created = models.DateTimeField(auto_now_add=True)`:
#    - Define un campo para almacenar la fecha y hora en que se creó el servicio.
#    - `auto_now_add=True` asegura que el valor de este campo se asignará automáticamente cuando se cree el objeto.

# 7. `updated = models.DateTimeField(auto_now_add=True)`:
#    - Define un campo para almacenar la fecha y hora de la última actualización del servicio.
#    - `auto_now_add=True` está configurado aquí, lo que debería haberse cambiado a `auto_now=True` para actualizar la fecha automáticamente cada vez que se guarde el objeto.

# 8. `class Meta:`:
#    - Dentro de esta clase se definen configuraciones adicionales para el modelo.

# 9. `verbose_name='servicio'`:
#    - Define un nombre más legible para la instancia del modelo en singular. Se utiliza en la interfaz de administración de Django.

# 10. `verbose_name_plural='servicios'`:
#    - Define el nombre en plural para la instancia del modelo. Se utiliza en la interfaz de administración de Django para mostrar "servicios" en lugar de "servicio".

# 11. `def __str__(self):`:
#    - Define el método especial `__str__`, que determina cómo se representa el objeto como una cadena de texto.
#    - En este caso, devuelve el `titulo` del servicio, lo que hace que se muestre el nombre del servicio en la interfaz de administración de Django.

# En resumen, este modelo crea una tabla `Servicio` en la base de datos con los campos `titulo`, `contenido`, `imagen`, `created` y `updated`. 
# Además, permite que cada servicio se represente de forma legible utilizando su `titulo` en el panel de administración.

   
        


