from tabnanny import verbose
from django.db import models

from django.contrib.auth import get_user_model 
from django.db.models import F,Sum, FloatField  
from tienda.models import Producto

User=get_user_model()

# Create your models here.

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at=models.DateTimeField(auto_now_add=True)  

    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"] or FloatField(0)

    def __str__(self):
        return self.id


    class Meta:
        db_table='pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']


class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre}'

    class Meta:
        db_table='lineapedidos'
        verbose_name='Línea Pedido'
        verbose_name_plural='Líneas Pedidos'
        ordering=['id']

# Este archivo define los modelos para los pedidos y las líneas de pedido en una tienda.

# 1. `from tabnanny import verbose`: 
#    - Este import no es necesario para el funcionamiento del código. 
#    - `verbose` se utiliza comúnmente en el contexto de las configuraciones de Django, pero `tabnanny` es una herramienta para detectar errores de indentación, y no es necesario en este archivo.
#    - Puedes eliminar esta línea sin que afecte el funcionamiento del código.

# 2. `from django.db import models`: 
#    - Importa las herramientas necesarias de Django para definir los modelos y los campos de la base de datos.

# 3. `from django.contrib.auth import get_user_model`: 
#    - Importa la función `get_user_model()` para obtener el modelo de usuario actual en Django (puede ser un modelo personalizado).

# 4. `from django.db.models import F, Sum, FloatField`: 
#    - Se importan funciones y clases para realizar operaciones sobre la base de datos, como el cálculo de sumas y la manipulación de campos numéricos.

# 5. `from tienda.models import Producto`: 
#    - Importa el modelo `Producto` desde la aplicación `tienda`, ya que cada pedido y línea de pedido hace referencia a un producto.

# 6. `User = get_user_model()`: 
#    - Asigna el modelo de usuario actual a la variable `User`. Esto es útil para que el modelo `Pedido` haga referencia al usuario autenticado.

# 7. `class Pedido(models.Model)`: 
#    - Define el modelo `Pedido`, que representa un pedido realizado por un usuario.
#    - Tiene los campos:
#        * `user`: Relación con el modelo `User`, el usuario que realiza el pedido.
#        * `created_at`: Fecha y hora en que se creó el pedido, asignada automáticamente.
#        * `total`: Propiedad que calcula el total del pedido basado en la suma de los precios y cantidades de las líneas de pedido asociadas.

# 8. `def total(self)`: 
#    - Una propiedad que calcula el total del pedido sumando el precio de los productos multiplicado por la cantidad de cada uno.
#    - Utiliza `F("precio")` y `F("cantidad")` para referirse a estos campos en las líneas de pedido, y la función `aggregate()` para obtener la suma total.

# 9. `class Meta`: 
#    - Define metadatos para el modelo `Pedido`, como el nombre de la tabla en la base de datos (`pedidos`), el nombre plural y el orden por `id`.

# 10. `class LineaPedido(models.Model)`: 
#    - Define el modelo `LineaPedido`, que representa una línea individual de un pedido, es decir, un producto y su cantidad en un pedido.
#    - Tiene los campos:
#        * `user`: Relación con el modelo `User`, el usuario que realiza el pedido.
#        * `producto`: Relación con el modelo `Producto`, el producto que se ha pedido.
#        * `pedido`: Relación con el modelo `Pedido`, el pedido al que pertenece esta línea.
#        * `cantidad`: Cantidad del producto solicitado en esta línea.
#        * `created_at`: Fecha y hora en que se creó la línea de pedido.

# 11. `def __str__(self)`: 
#    - Método que define cómo se representará cada línea de pedido como cadena, mostrando la cantidad y el nombre del producto.

# 12. `class Meta`: 
#    - Define metadatos para el modelo `LineaPedido`, como el nombre de la tabla (`lineapedidos`), el nombre plural y el orden por `id`.

# En resumen, este archivo define dos modelos esenciales para el sistema de pedidos: 
# 1. `Pedido`: Representa un pedido realizado por un usuario.
# 2. `LineaPedido`: Representa cada producto individual en un pedido.

