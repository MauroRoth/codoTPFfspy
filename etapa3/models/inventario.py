from .producto import Producto
from ..dbconfig import *

class Inventario:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
    
    # Este método permite crear objetos de la clase "Producto" y agregarlos al inventario.
    def agregar_producto(self, codigo, descripcion, cantidad, precio):
        producto_existente = self.consultar_producto(codigo)
        if producto_existente:
            print("Ya existe un producto con ese código.")
            return False
        nuevo_producto = Producto(codigo, descripcion, cantidad, precio)
        sql = f'INSERT INTO productos VALUES ({codigo}, "{descripcion}",{cantidad}, {precio});'
        self.cursor.execute(sql)
        self.conexion.commit()
        return True
    
    # Este método permite consultar datos de productos que están en el inventario
    # Devuelve el producto correspondiente al código proporcionado o False si no existe.
    def consultar_producto(self, codigo):
        sql = f'SELECT * FROM productos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, cantidad, precio = row
            return Producto(codigo, descripcion, cantidad, precio)
        return False
    
    # Este método permite modificar datos de productos que están en el inventario
    # Utiliza el método consultar_producto del inventario y modificar del producto.
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio):
        producto = self.consultar_producto(codigo)
        if producto:
            producto.modificar(nueva_descripcion, nueva_cantidad, nuevo_precio)
            sql = f'UPDATE productos SET descripcion = "{nueva_descripcion}", cantidad = {nueva_cantidad}, precio = {nuevo_precio} WHERE codigo = {codigo};'
            self.cursor.execute(sql)
            self.conexion.commit()
     
    # Este método elimina el producto indicado por codigo de la lista mantenida en el inventario.
    def eliminar_producto(self, codigo):
        sql = f'DELETE FROM productos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            print(f'Producto {codigo} eliminado.')
            self.conexion.commit()
        else:
            print(f'Producto {codigo} no encontrado.')
 
    # Este método imprime en la terminal una lista con los datos de los productos que figuran en el inventario.
    def listar_productos(self):
        print("-"*50)
        print("Lista de productos en el inventario:")
        print("Código\tDescripción\tCant\tPrecio")
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        for row in rows:
            codigo, descripcion, cantidad, precio = row
            print(f'{codigo}\t{descripcion}\t{cantidad}\t{precio}')
        print("-"*50)
