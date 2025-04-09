class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        # Obtener el carrito de la sesión, si no existe, inicializarlo vacío
        carro = self.session.get("carro")
        if not carro:
            self.carro = self.session["carro"] = {}
        else:
            self.carro = carro  # Asignar el carrito existente a self.carro

    def agregar(self, producto):
        producto_id = str(producto.id)  # Asegurarse de usar str para la clave
        if producto_id not in self.carro:
            self.carro[producto_id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),  # Convertir precio a string
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            self.carro[producto_id]["cantidad"] += 1
            self.carro[producto_id]["precio"] = float(self.carro[producto_id]["precio"]) + float(producto.precio)
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)  # Asegurarse de usar str para la clave
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def restar_producto(self, producto):
        producto_id = str(producto.id)  # Asegurarse de usar str para la clave
        if producto_id in self.carro:
            self.carro[producto_id]["cantidad"] -= 1
            self.carro[producto_id]["precio"] = float(self.carro[producto_id]["precio"]) - float(producto.precio)
            if self.carro[producto_id]["cantidad"] < 1:
                self.eliminar(producto)  # Eliminar si la cantidad es menor que 1
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
