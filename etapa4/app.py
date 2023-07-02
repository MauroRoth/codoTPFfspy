import sqlite3
from flask import Flask, jsonify, request
from .dbconfig import *
from .models.carrito import Carrito
from .models.inventario import Inventario

# Crear la base de datos y la tabla si no existen
create_database()

# Crear una instancia de la clase Inventario
mi_inventario = Inventario()
# Agregar productos al inventario
mi_inventario.agregar_producto(1, "Producto 1", 10, 19.99)
mi_inventario.agregar_producto(2, "Producto 2", 5, 9.99)
mi_inventario.agregar_producto(3, "Producto 3", 15, 29.99)
mi_inventario.agregar_producto(4, "Producto 4", 60, 85.6)

app = Flask(__name__)

carrito = Carrito() # Instanciamos un carrito
inventario = Inventario() # Instanciamos un inventario

# Ruta para obtener el index
@app.route('/')
def index():
    return '<h1>API de Inventario</h1>'

# Ruta para obtener la lista de productos del inventario
@app.route('/productos', methods=['GET'])
def obtener_productos():
    print(inventario.listar_productos())
    return jsonify(inventario.listar_productos())

# Ruta para obtener los datos de un producto según su código
@app.route('/productos/<int:codigo>', methods=['GET'])
def obtener_producto(codigo):
    producto = inventario.consultar_producto(codigo)
    print(producto)
    if producto:
        return jsonify({
            'codigo': producto.codigo,
            'descripcion': producto.descripcion,
            'cantidad': producto.cantidad,
            'precio': producto.precio
        }), 200
    return jsonify({'message': 'Producto no encontrado.'}), 404

# Ruta para agregar un producto al inventario
@app.route('/productos', methods=['POST'])
def agregar_producto():
    codigo = request.json.get('codigo')
    descripcion = request.json.get('descripcion')
    cantidad = request.json.get('cantidad')
    precio = request.json.get('precio')
    if inventario.agregar_producto(codigo, descripcion, cantidad, precio):
        return jsonify({'message': 'Ya existe un producto con ese código.'}), 400
    else:
        return jsonify({'message': 'Producto agregado correctamente.'}), 200

# Ruta para modificar un producto del inventario
@app.route('/productos/<int:codigo>', methods=['PUT'])
def modificar_producto(codigo):
    nueva_descripcion = request.json.get('descripcion')
    nueva_cantidad = request.json.get('cantidad')
    nuevo_precio = request.json.get('precio')
    return inventario.modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio)

# Ruta para eliminar un producto del inventario
@app.route('/productos/<int:codigo>', methods=['DELETE'])
def eliminar_producto(codigo):
    return inventario.eliminar_producto(codigo)

# Ruta para agregar un producto al carrito
@app.route('/carrito', methods=['POST'])
def agregar_carrito():
    codigo = request.json.get('codigo')
    cantidad = request.json.get('cantidad')
    inventario = Inventario()
    return carrito.agregar(codigo, cantidad, inventario)

# Ruta para quitar un producto del carrito
@app.route('/carrito', methods=['DELETE'])
def quitar_carrito():
    codigo = request.json.get('codigo')
    cantidad = request.json.get('cantidad')
    inventario = Inventario()
    return carrito.quitar(codigo, cantidad, inventario)

# Ruta para obtener el contenido del carrito
@app.route('/carrito', methods=['GET'])
def obtener_carrito():
    return carrito.mostrar()

# Finalmente, si estamos ejecutando este archivo, lanzamos app.
if __name__ == '__main__':
    app.run(debug=True)
