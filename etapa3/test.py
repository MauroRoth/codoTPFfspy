from .dbconfig import *
from .models.inventario import Inventario
from .models.carrito import Carrito

# Programa principal

# Crear la base de datos y la tabla si no existen
create_database()
# Crear una instancia de la clase Inventario
mi_inventario = Inventario()
# Agregar productos al inventario
mi_inventario.agregar_producto(1, "Producto 1", 10, 19.99)
mi_inventario.agregar_producto(2, "Producto 2", 5, 9.99)
mi_inventario.agregar_producto(3, "Producto 3", 15, 29.99)
mi_inventario.agregar_producto(4, "Producto 4", 60, 85.6)
# Consultar algún producto del inventario
print(mi_inventario.consultar_producto(3)) #Existe, se muestra la dirección de memoria
print(mi_inventario.consultar_producto(4)) #No existe, se muestra False
# Listar los productos del inventario
mi_inventario.listar_productos()

print('='*50)#===========================================================

# Modificar un producto del inventario
mi_inventario.modificar_producto(2, "Mouse Rojo", 10, 19.99)
# Listar nuevamente los productos del inventario para ver la modificación
mi_inventario.listar_productos()
# Eliminar un producto
mi_inventario.eliminar_producto(3)
# Listar nuevamente los productos del inventario para ver la eliminación
mi_inventario.listar_productos()

print('@'*50)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Crear una instancia de la clase Carrito
mi_carrito = Carrito()
# Agregar 2 unidades del producto con código 1 al carrito
mi_carrito.agregar(1, 2, mi_inventario)
# Agregar 1 unidad del producto con código 2 al carrito
mi_carrito.agregar(2, 1, mi_inventario)
# Mostrar el contenido del carrito y del inventario
mi_carrito.mostrar()
mi_inventario.listar_productos()

print('&'*50)#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Quitar 1 unidad del producto con código 1 al carrito y 1 unidad del producto con código 2 al carrito
mi_carrito.quitar(1, 1, mi_inventario)
mi_carrito.quitar(2, 1, mi_inventario)
# Mostrar el contenido del carrito y del inventario
mi_carrito.mostrar()
mi_inventario.listar_productos()