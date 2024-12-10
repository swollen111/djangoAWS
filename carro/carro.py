class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
       
        self.carro=carro

    def agregar(self,producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["precio"]=float(value["precio"])-producto.precio
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True

# Esta clase define la lógica para gestionar el carrito de compras de un usuario en la sesión de Django.

# 1. `class Carro:`:
#    - Define la clase `Carro`, que maneja la interacción con el carrito de compras almacenado en la sesión del usuario.
#    - La clase proporciona métodos para agregar productos, eliminar productos, restar la cantidad de productos y limpiar el carrito.

# 2. `def __init__(self, request):`:
#    - Constructor de la clase que recibe el objeto `request` como parámetro.
#    - Inicializa los atributos `request`, `session` (accediendo a la sesión de Django) y `carro` (que obtiene los datos del carrito almacenados en la sesión).
#    - Si no existe un carrito en la sesión, se crea un carrito vacío (`{}`).

# 3. `def agregar(self, producto):`:
#    - Método que agrega un producto al carrito. Si el producto no está en el carrito, lo agrega con una cantidad de 1.
#    - Si el producto ya está en el carrito, incrementa su cantidad y actualiza su precio (sumando el precio del producto).
#    - Al final, guarda los cambios en la sesión mediante el método `guardar_carro()`.

# 4. `def guardar_carro(self):`:
#    - Método que guarda los cambios realizados en el carrito en la sesión, asegurándose de que la sesión se marque como modificada.
#    - Esto permite que los cambios en el carrito persistan entre las solicitudes.

# 5. `def eliminar(self, producto):`:
#    - Método que elimina un producto del carrito según su ID.
#    - Si el producto está en el carrito, se elimina y luego se guarda el carrito actualizado en la sesión.

# 6. `def restar_producto(self, producto):`:
#    - Método que resta uno de la cantidad de un producto en el carrito.
#    - Si la cantidad se reduce a menos de 1, el producto se elimina del carrito.
#    - Después de modificar la cantidad, se guarda el carrito actualizado.

# 7. `def limpiar_carro(self):`:
#    - Método que limpia completamente el carrito, eliminando todos los productos del mismo.
#    - Después de limpiar el carrito, guarda los cambios en la sesión.

# En resumen, la clase `Carro` gestiona el carrito de compras de un usuario, permitiendo agregar productos, eliminar productos, ajustar cantidades y limpiar el carrito.
# Los cambios se almacenan en la sesión del usuario, lo que garantiza que el carrito persista durante las distintas solicitudes del usuario.
