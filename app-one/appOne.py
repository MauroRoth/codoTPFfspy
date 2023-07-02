import sqlite3
from flask import Flask, jsonify, request, render_template

class Producto:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self, codigo, descripcion, cantidad, precio):
        self.codigo = codigo # Código
        self.descripcion = descripcion # Descripción
        self.cantidad = cantidad # Cantidad disponible (stock)
        self.precio = precio # Precio
    # Este método permite modificar un producto.
    def modificar(self, nueva_descripcion, nueva_cantidad, nuevo_precio):
        self.descripcion = nueva_descripcion # Modifica la descripción
        self.cantidad = nueva_cantidad # Modifica la cantidad
        self.precio = nuevo_precio # Modifica el precio

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
        sql = f'INSERT INTO productos VALUES ({codigo}, "{descripcion}", {cantidad}, {precio});'
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
        lista = []
        for row in rows:
            codigo, descripcion, cantidad, precio = row
            fila = {'código':codigo, 'descripción': descripcion, 'cantidad': cantidad, 'precio': precio}
            lista.append(fila)
            print(f'{codigo}\t{descripcion}\t{cantidad}\t{precio}')
        print("-"*50)
        return lista

class Carrito:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
        self.items = []
 
    # Este método permite agregar productos del inventario al carrito.
    def agregar(self, codigo, cantidad, inventario):
        producto = inventario.consultar_producto(codigo)
        if producto is False:
            print("El producto no existe.")
            return False
        if producto.cantidad < cantidad:
            print("Cantidad en stock insuficiente.")
            return False
        for item in self.items:
            if item.codigo == codigo:
                item.cantidad += cantidad
                sql = f'UPDATE productos SET cantidad = cantidad - {cantidad} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return True
        nuevo_item = Producto(codigo, producto.descripcion, cantidad, producto.precio)
        self.items.append(nuevo_item)
        sql = f'UPDATE productos SET cantidad = cantidad - {cantidad} WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        self.conexion.commit()
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
                sql = f'UPDATE productos SET cantidad = cantidad + {cantidad} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return True
        print("El producto no se encuentra en el carrito.")
        return False

    def mostrar(self):
        print("-"*50)
        print("Lista de productos en el carrito:")
        print("Código\tDescripción\tCant\tPrecio")
        for item in self.items:
            print(f'{item.codigo}\t{item.descripcion}\t{item.cantidad}\t{item.precio}')
        print("-"*50)

# Configurar la conexión a la base de datos SQLite
DATABASE = 'etapa4/inventario.db'
def get_db_connection():
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'productos' si no existe
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            codigo INTEGER PRIMARY KEY,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        ) ''')
    conn.commit()
    cursor.close()
    conn.close()

# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database():
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    conn.close()
    create_table()

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

# RUTAS
@app.route('/') # obtiene el index
def index():
    constante = 852
    return render_template('index.html', constante = constante)

@app.route('/productos', methods=['GET']) # lista de productos del inventario
def obtener_productos():
    print(inventario.listar_productos())
    return jsonify(inventario.listar_productos())

# obtener los datos de un producto según su código
@app.route('/productos/<int:codigo>', methods=['GET']) # datos de un producto según código
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

@app.route('/productos', methods=['POST']) # agrega un producto al inventario
def agregar_producto():
    codigo = request.json.get('codigo')
    descripcion = request.json.get('descripcion')
    cantidad = request.json.get('cantidad')
    precio = request.json.get('precio')
    if inventario.agregar_producto(codigo, descripcion, cantidad, precio):
        return jsonify({'message': 'Ya existe un producto con ese código.'}), 400
    else:
        return jsonify({'message': 'Producto agregado correctamente.'}), 200

@app.route('/productos/<int:codigo>', methods=['PUT']) # modifica un producto del inventario
def modificar_producto(codigo):
    nueva_descripcion = request.json.get('descripcion')
    nueva_cantidad = request.json.get('cantidad')
    nuevo_precio = request.json.get('precio')
    return inventario.modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio)

@app.route('/productos/<int:codigo>', methods=['DELETE']) # elimina un producto del inventario
def eliminar_producto(codigo):
    return inventario.eliminar_producto(codigo)

@app.route('/carrito', methods=['POST']) # agrega un producto al carrito
def agregar_carrito():
    codigo = request.json.get('codigo')
    cantidad = request.json.get('cantidad')
    inventario = Inventario()
    return carrito.agregar(codigo, cantidad, inventario)

@app.route('/carrito', methods=['DELETE']) # quita un producto del carrito
def quitar_carrito():
    codigo = request.json.get('codigo')
    cantidad = request.json.get('cantidad')
    inventario = Inventario()
    return carrito.quitar(codigo, cantidad, inventario)

@app.route('/carrito', methods=['GET']) # contenido del carrito
def obtener_carrito():
    return carrito.mostrar()

# Finalmente, si estamos ejecutando este archivo, lanzamos app.
if __name__ == '__main__':
    app.run(debug=True)