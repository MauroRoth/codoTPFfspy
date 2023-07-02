from ..models.inventario import Inventario
from ..models.producto import Producto

def testInventario():
    # Programa principal

    # Crear una instancia de la clase Inventario
    mi_inventario = Inventario()

    # Agregar productos
    mi_inventario.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500)
    mi_inventario.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500)
    mi_inventario.agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500)
    mi_inventario.agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500)
    mi_inventario.agregar_producto(5, 'Mouse Pad color azul', 5, 500)

    # Consultar un producto
    producto = mi_inventario.consultar_producto(3)
    if producto != False:
        print(f'Producto encontrado:\nCódigo: {producto.codigo}\nDescripción:{producto.descripcion}\nCantidad: {producto.cantidad}\nPrecio:{producto.precio}')
    else:
        print("Producto no encontrado.")

    # Modificar un producto
    mi_inventario.modificar_producto(3, 'Monitor LCD 24 pulgadas', 5, 62000)

    # Listar todos los productos
    mi_inventario.listar_productos()

    # Eliminar un producto
    mi_inventario.eliminar_producto(2)

    # Confirmamos que haya sido eliminado
    mi_inventario.listar_productos()