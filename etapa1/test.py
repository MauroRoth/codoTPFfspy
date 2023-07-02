from funciones import *
# Agregamos productos a la lista:
agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500)
agregar_producto(2, 'Mouse USB 3 botones', 5, 2500)
agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500)
agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500)
agregar_producto(5, 'Pad mouse', 5, 500)
# eliminar_producto(5) # Eliminamos un producto del stock.
# Consultar un producto por su código
# producto = consultar_producto(1)
# if producto:
# print(f"Producto encontrado: {producto['descripcion']}")
# else:
# print("Producto no encontrado.")
# Modificar un producto por su código
# modificar_producto(1, 'Teclado mecánico 62 teclas', 20, 34000)
# Listamos todos los productos en pantalla
listar_productos()
# Agregamos productos al carrito
agregar_al_carrito(1, 2)
agregar_al_carrito(2, 1)
# agregar_al_carrito(30, 1) # intentamos agregar un producto inexistente
# Intentar agregar un producto con cantidad insuficiente
# agregar_al_carrito(1, 150)
# Quitar un producto del carrito
quitar_del_carrito(1, 1)
# Mostrar el contenido del carrito
mostrar_carrito()