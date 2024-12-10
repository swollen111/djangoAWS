from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):

    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria,"posts": posts })

# Este archivo define vistas relacionadas con la funcionalidad del blog en la aplicación Django.

# 1. `blog(request)`:
#    - Obtiene todos los objetos de la clase `Post` almacenados en la base de datos (`Post.objects.all()`).
#    - Renderiza la plantilla `blog/blog.html`, pasando los posts como contexto bajo la clave `posts`.
#    - Esta vista se utiliza para mostrar una lista completa de publicaciones del blog.

# 2. `categoria(request, categoria_id)`:
#    - Obtiene una categoría específica basada en el `categoria_id` recibido como argumento (`Categoria.objects.get(id=categoria_id)`).
#    - Filtra los posts que pertenecen a la categoría seleccionada (`Post.objects.filter(categorias=categoria)`).
#    - Renderiza la plantilla `blog/categoria.html`, pasando como contexto:
#        * `categoria`: La categoría seleccionada.
#        * `posts`: Los posts asociados a dicha categoría.
#    - Esta vista permite mostrar las publicaciones agrupadas por categorías.

# En resumen, este archivo contiene las vistas para:
# - Mostrar todas las publicaciones del blog.
# - Filtrar y mostrar publicaciones basadas en una categoría específica.
