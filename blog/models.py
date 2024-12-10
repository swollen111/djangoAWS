from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="blog", null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo

# Este archivo define los modelos de datos relacionados con el blog en la aplicación Django.

# 1. `class Categoria(models.Model)`:
#    - Representa una categoría del blog.
#    - Campos:
#        * `nombre`: Un campo de texto con un límite de 50 caracteres para el nombre de la categoría.
#        * `created`: Almacena la fecha y hora de creación del objeto (se genera automáticamente).
#        * `updated`: Almacena la fecha y hora de la última actualización del objeto (se genera automáticamente).
#    - Clase Meta:
#        * `verbose_name` y `verbose_name_plural`: Especifican nombres amigables para la categoría en singular y plural en el panel de administración.
#    - Método `__str__`: Devuelve el nombre de la categoría al convertir el objeto a cadena, útil en interfaces administrativas o de depuración.

# 2. `class Post(models.Model)`:
#    - Representa una publicación del blog.
#    - Campos:
#        * `titulo`: Título del post, un texto limitado a 50 caracteres.
#        * `contenido`: Contenido del post, también limitado a 50 caracteres (podría ser cambiado a `TextField` para contenido más largo).
#        * `imagen`: Imagen opcional asociada al post, almacenada en el directorio `blog`.
#        * `autor`: Relación con el modelo `User`, indicando el autor del post. Si el usuario es eliminado, también lo será el post (`on_delete=models.CASCADE`).
#        * `categorias`: Relación muchos-a-muchos con el modelo `Categoria`, indicando las categorías asociadas al post.
#        * `created`: Fecha y hora de creación del post (se genera automáticamente).
#        * `updated`: Fecha y hora de la última actualización (se genera automáticamente).
#    - Clase Meta:
#        * `verbose_name` y `verbose_name_plural`: Nombres amigables para el post en singular y plural en el panel de administración.
#    - Método `__str__`: Devuelve el título del post al convertir el objeto a cadena.

# En resumen, este archivo define dos modelos principales para el blog:
# - `Categoria`: Para clasificar las publicaciones.
# - `Post`: Para almacenar la información de las publicaciones, incluyendo título, contenido, autor, categorías y una imagen opcional.
