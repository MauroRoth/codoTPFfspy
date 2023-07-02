from ..models.producto import Producto
from ..models.inventario import Inventario
from ..models.carrito import Carrito

def testCarrito():
    # Programa principal
    # ---------------------------------------------------------------------
    # Ejemplo de uso de las clases y objetos definidos antes:
    # ---------------------------------------------------------------------
    # Crear una instancia de la clase Inventario
    mi_inventario = Inventario()
    # Crear una instancia de la clase Carrito
    mi_carrito = Carrito()
    # Crear 3 productos y agregarlos al inventario
    mi_inventario.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500)
    mi_inventario.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500)
    mi_inventario.agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500)
    # Listar todos los productos del inventario
    mi_inventario.listar_productos()
    # Agregar 2 productos al carrito
    mi_carrito.agregar(1, 2, mi_inventario) # Agregar 2 unidades del producto con código 1 al carrito
    mi_carrito.agregar(3, 4, mi_inventario) # Agregar 1 unidad del producto con código 3 al carrito
    mi_carrito.quitar (1, 1, mi_inventario) # Quitar 1 unidad del producto con código 1 al carrito
    # Listar todos los productos del carrito
    mi_carrito.mostrar()
    # Quitar 1 producto al carrito
    mi_carrito.quitar (1, 1, mi_inventario) # Quitar 1 unidad del producto con código 1 al carrito
    # Listar todos los productos del carrito
    mi_carrito.mostrar()
    # Mostramos el inventario
    mi_inventario.listar_productos()