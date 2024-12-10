from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

# Este archivo registra los modelos `Categoria` y `Post` en el panel de administración de Django, para que puedan ser gestionados desde la interfaz de administración.

# 1. `class CategoriaAdmin(admin.ModelAdmin)`:
#    - Configura cómo se gestionará el modelo `Categoria` en el panel de administración de Django.
#    - `readonly_fields=('created', 'updated')`: Hace que los campos `created` y `updated` sean solo lectura, es decir, no podrán ser editados directamente desde la interfaz de administración.

# 2. `class PostAdmin(admin.ModelAdmin)`:
#    - Configura cómo se gestionará el modelo `Post` en el panel de administración de Django.
#    - `readonly_fields=('created', 'updated')`: Similar a la configuración de `CategoriaAdmin`, hace que los campos `created` y `updated` del modelo `Post` sean solo lectura.

# 3. `admin.site.register(Categoria, CategoriaAdmin)`:
#    - Registra el modelo `Categoria` con la configuración personalizada de `CategoriaAdmin` para que se gestione en el panel de administración.

# 4. `admin.site.register(Post, PostAdmin)`:
#    - Registra el modelo `Post` con la configuración personalizada de `PostAdmin` para que se gestione en el panel de administración.

# En resumen, este archivo personaliza la interfaz de administración para los modelos `Categoria` y `Post`, limitando la edición de ciertos campos y facilitando su gestión desde el panel de administración de Django.
