from .producto import Producto

class Inventario:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.productos = [] # Lista de productos en el inventario (variable de clase)
    
    # Este método permite crear objetos de la clase "Producto" y agregarlos al inventario.
    def agregar_producto(self, codigo, descripcion, cantidad, precio):
        nuevo_producto = Producto(codigo, descripcion, cantidad, precio)
        self.productos.append(nuevo_producto) # Agrega un nuevo producto a la lista
    
    # Este método permite consultar datos de productos que están en el inventario
    # Devuelve el producto correspondiente al código proporcionado o False si no existe.
    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto # Retorna un objeto
        return False
    
    # Este método permite modificar datos de productos que están en el inventario
    # Utiliza el método consultar_producto del inventario y modificar del producto.
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio):
        producto = self.consultar_producto(codigo)
        if producto:
            producto.modificar(nueva_descripcion, nueva_cantidad, nuevo_precio)
    
    # Este método elimina el producto indicado por codigo de la lista mantenida en el inventario.
    def eliminar_producto(self, codigo):
        eliminar = False
        for producto in self.productos:
            if producto.codigo == codigo:
                eliminar = True
            producto_eliminar = producto
        if eliminar == True:
            self.productos.remove(producto_eliminar)
            print(f'Producto {codigo} eliminado.')
        else:
            print(f'Producto {codigo} no encontrado.')
    
    # Este método imprime en la terminal una lista con los datos de los productos que figuran en el inventario.
    def listar_productos(self):
        print("-"*50)
        print("Lista de productos en el inventario:")
        print("Código\tDescripción\t\tCant\tPrecio")
        for producto in self.productos:
            print(f'{producto.codigo}\t{producto.descripcion}\t{producto.cantidad}\t{producto.precio}')
        print("-"*50)