from .testProducto import testProducto
from .testInventario import testInventario
from .testCarrito import testCarrito

bandera = 1
while bandera == 1:
    opcion = int(input("0: Exit - 1:Test 1 - 2:Test 2 - 3:Test 3 :"))
    if opcion == 1: 
        testProducto()
    if opcion == 2:
        testInventario()
    if opcion == 3:
        testCarrito()
    if opcion == 0:
        bandera = opcion