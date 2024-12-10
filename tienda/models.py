from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

  

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

# 1. `from django.db import models`:
#    - Importa el módulo `models` de Django, que proporciona las herramientas necesarias para definir modelos en la base de datos.

# 2. `class CategoriaProd(models.Model):`:
#    - Define el modelo `CategoriaProd`, que representa una categoría de productos en la tienda.
#    - Hereda de `models.Model`, lo que indica que es un modelo de Django que se almacenará en la base de datos.

# 3. `nombre = models.CharField(max_length=50)`:
#    - Define un campo `nombre`, que es un campo de texto con un límite de 50 caracteres.
#    - Representa el nombre de la categoría de productos.

# 4. `created = models.DateTimeField(auto_now_add=True)`:
#    - Define un campo `created` para almacenar la fecha y hora en que se creó el registro.
#    - `auto_now_add=True` asegura que se establezca automáticamente la fecha y hora cuando se crea la categoría.

# 5. `updated = models.DateTimeField(auto_now_add=True)`:
#    - Define un campo `updated` para almacenar la fecha y hora en que se actualizó el registro.
#    - `auto_now_add=True` asegura que se establezca automáticamente la fecha y hora al momento de la creación, aunque generalmente este campo debería ser `auto_now=True` para registrar las actualizaciones.

# 6. `class Meta:`:
#    - Define metadatos para el modelo.
#    - `verbose_name` y `verbose_name_plural` definen los nombres legibles para el modelo en singular y plural, respetivamente.

# 7. `def __str__(self):`:
#    - Define un método especial `__str__` que devuelve el nombre de la categoría cuando se representa el objeto como cadena de texto.
  
# 8. `class Producto(models.Model):`:
#    - Define el modelo `Producto`, que representa un producto en la tienda.
#    - Hereda de `models.Model`, indicando que también se almacenará en la base de datos.

# 9. `nombre = models.CharField(max_length=50)`:
#    - Define un campo `nombre` para almacenar el nombre del producto, con un máximo de 50 caracteres.

# 10. `categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)`:
#     - Define una relación de clave externa (`ForeignKey`) con el modelo `CategoriaProd`, que vincula cada producto con una categoría.
#     - `on_delete=models.CASCADE` asegura que si una categoría se elimina, todos los productos asociados a ella también sean eliminados.

# 11. `imagen = models.ImageField(upload_to="tienda", null=True, blank=True)`:
#     - Define un campo `imagen` para almacenar una imagen del producto.
#     - `upload_to="tienda"` indica que las imágenes se almacenarán en una carpeta llamada `tienda`.
#     - `null=True, blank=True` permiten que el campo sea opcional.

# 12. `precio = models.FloatField()`:
#     - Define un campo `precio` para almacenar el precio del producto, utilizando un número de punto flotante.

# 13. `disponibilidad = models.BooleanField(default=True)`:
#     - Define un campo `disponibilidad` para indicar si el producto está disponible para la venta.
#     - `default=True` establece que el producto estará disponible por defecto.

# 14. `created = models.DateTimeField(auto_now_add=True)`:
#     - Define un campo `created` para almacenar la fecha y hora en que se creó el producto, con la opción de establecerla automáticamente.

# 15. `updated = models.DateTimeField(auto_now_add=True)`:
#     - Define un campo `updated` para almacenar la fecha y hora en que se actualizó el producto. De nuevo, este campo debería tener `auto_now=True` en lugar de `auto_now_add=True`.

# 16. `class Meta:`:
#     - Define metadatos para el modelo `Producto`.
#     - `verbose_name` y `verbose_name_plural` asignan nombres legibles en singular y plural para el modelo.

# 17. `class Producto(models.Model):`:
#     - Define la clase `Producto`, que será utilizada para crear y gestionar los productos en la tienda.

# En resumen, este archivo define dos modelos de base de datos: `CategoriaProd` (para las categorías de productos) y `Producto` (para los productos que se venden en la tienda). Los productos están vinculados a las categorías, y cada producto tiene atributos como nombre, imagen, precio, disponibilidad y fechas de creación y actualización.
