# tienda.py

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        """Reduce el stock si hay suficiente cantidad disponible."""
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} x {self.nombre}")
        else:
            print(f"No hay stock suficiente de {self.nombre}.")

    def reponer(self, cantidad):
        """Aumenta el stock del producto."""
        self.stock += cantidad
        print(f"Stock de {self.nombre} aumentado en {cantidad} unidades.")

    def mostrar_info(self):
        """Muestra información del producto."""
        print(f"{self.nombre} | Precio: {self.precio} | Stock: {self.stock}")


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un nuevo producto a la tienda."""
        self.productos.append(producto)

    def listar_productos(self):
        """Muestra todos los productos disponibles."""
        print(f"=== Productos en la tienda {self.nombre} ===")
        for p in self.productos:
            p.mostrar_info()

    def vender_producto(self, nombre_producto, cantidad):
        """Busca un producto por nombre y realiza la venta."""
        for p in self.productos:
            if p.nombre == nombre_producto:
                p.vender(cantidad)
                return
        print(f"El producto {nombre_producto} no existe en la tienda.")


if __name__ == "__main__":
    tienda = Tienda("TechStore")
    p1 = Producto("Mouse", 10.0, 15)
    p2 = Producto("Teclado", 20.0, 10)

    tienda.agregar_producto(p1)
    tienda.agregar_producto(p2)

    tienda.listar_productos()
    tienda.vender_producto("Mouse", 3)
    tienda.vender_producto("Mouse", 20)
    tienda.listar_productos()
