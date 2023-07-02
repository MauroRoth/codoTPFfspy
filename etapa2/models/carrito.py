from .producto import Producto
from .inventario import Inventario

class Carrito:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.items = [] # Lista de items en el carrito (variable de clase)
    
    # Este método permite agregar productos del inventario al carrito.
    def agregar(self, codigo, cantidad, inventario):
        # Nos aseguramos que el producto esté en el inventario
        producto = inventario.consultar_producto(codigo)
        if producto is False:
            print("El producto no existe.")
            return False
    
        # Verificamos que la cantidad en stock sea suficiente
        if producto.cantidad < cantidad:
            print("Cantidad en stock insuficiente.")
            return False
        
        # Si existe y hay stock, vemos si ya existe en el carrito.
        for item in self.items:
            if item.codigo == codigo:
                item.cantidad += cantidad
                # Actualizamos la cantidad en el inventario
                producto = inventario.consultar_producto(codigo)
                producto.modificar(producto.descripcion, producto.cantidad - cantidad, producto.precio)
                return True

        # Si no existe en el carrito, lo agregamos como un nuevo item.
        nuevo_item = Producto(codigo, producto.descripcion, cantidad, producto.precio)
        self.items.append(nuevo_item)
        # Actualizamos la cantidad en el inventario
        producto = inventario.consultar_producto(codigo)
        producto.modificar(producto.descripcion, producto.cantidad - cantidad, producto.precio)
        return True

    # Este método quita unidades de un elemento del carrito, o lo elimina.
    def quitar(self, codigo, cantidad, inventario):
        for item in self.items:
            if item.codigo == codigo:
                if cantidad > item.cantidad:
                    print("Cantidad a quitar mayor a la cantidad en el carrito.")
                    return False
                item.cantidad -= cantidad
                if item.cantidad == 0:
                    self.items.remove(item)
                    # Actualizamos la cantidad en el inventario
                    producto = inventario.consultar_producto(codigo)
                    producto.modificar(producto.descripcion, producto.cantidad + cantidad, producto.precio)
                    return True
        # Si el bucle finaliza sin novedad, es que ese producto NO ESTA en el carrito.
        print("El producto no se encuentra en el carrito.")
        return False
        
    def mostrar(self):
        print("-"*50)
        print("Lista de productos en el carrito:")
        print("Código\tDescripción\t\tCant\tPrecio")
        for item in self.items:
            print(f'{item.codigo}\t{item.descripcion}\t{item.cantidad}\t{item.precio}')
        print("-"*50)