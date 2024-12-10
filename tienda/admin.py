from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class ProductoAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)

# 1. `from django.contrib import admin`:
#    - Importa el módulo `admin` de Django, que se utiliza para registrar y personalizar modelos en el sitio de administración de Django.

# 2. `from .models import CategoriaProd, Producto`:
#    - Importa los modelos `CategoriaProd` y `Producto` desde el archivo `models.py` de la aplicación.
#    - Estos modelos representan las entidades de categorías de productos y productos, respectivamente.

# 3. `class CategoriaProdAdmin(admin.ModelAdmin):`:
#    - Define una clase `CategoriaProdAdmin` que hereda de `admin.ModelAdmin`, utilizada para personalizar la apariencia y comportamiento de `CategoriaProd` en el panel de administración de Django.
#    - La clase se puede usar para modificar el registro del modelo, como agregar campos de solo lectura o filtros personalizados.

# 4. `readonly_fields=("created","updated")`:
#    - Define que los campos `created` y `updated` serán solo de lectura en el panel de administración.
#    - Estos campos se llenan automáticamente con la fecha de creación y actualización, por lo que no deben ser editados directamente.

# 5. `class ProductoAdmin(admin.ModelAdmin):`:
#    - Define una clase `ProductoAdmin` que hereda de `admin.ModelAdmin` para personalizar cómo se muestra y gestiona el modelo `Producto` en el sitio de administración de Django.

# 6. `readonly_fields=("created","updated")`:
#    - Establece que los campos `created` y `updated` en el modelo `Producto` también serán solo de lectura en el panel de administración.

# 7. `admin.site.register(CategoriaProd, CategoriaProdAdmin)`:
#    - Registra el modelo `CategoriaProd` en el sitio de administración de Django, utilizando la configuración personalizada `CategoriaProdAdmin`.

# 8. `admin.site.register(Producto, ProductoAdmin)`:
#    - Registra el modelo `Producto` en el sitio de administración de Django, utilizando la configuración personalizada `ProductoAdmin`.

# En resumen, este archivo configura la interfaz de administración para los modelos `CategoriaProd` y `Producto`, asegurando que los campos `created` y `updated` sean solo de lectura, y que se gestionen correctamente en el panel de administración.
