# Definimos una lista para almacenar los productos.
# Es una lista de diccionarios.
productos = []
# Definir un segundo arreglo para el carrito de compras
carrito = []

def agregar_producto(codigo, descripcion, cantidad, precio):
    # Creamos un diccionario con los datos del producto...
    nuevo_producto = {
        'codigo': codigo,'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio
    }
    # Y lo agregamos a nuestro arreglo.
    productos.append(nuevo_producto)
    return True

def consultar_producto(codigo):
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
        # Refresamos el diccionario correspondiente.
            return producto
    # Si el bucle finaliza sin encontrar el producto,
    # regresamos "falso."
    return False

def modificar_producto(codigo, nueva_descripcion, nueva_cantidad,nuevo_precio):
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
        # ...actualizamos los valores de cada clave del diccionario
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
        # Como no hay otro producto con ese código, salimos del bucle.
        return True
    # Si llegamos aqui, el producto no existe.
    return False

def listar_productos():
    # Recorremos la lista de productos...
    print("-"*30)
    for producto in productos:
        # Y mostramos los datos de cada uno de ellos.
        print(f"Código: {producto['codigo']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")
        print("-"*30)

def eliminar_producto(codigo):
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # ...lo quitamos de la lista.
            productos.remove(producto)
        # Como no hay otro producto con ese código, salimos del bucle.
        return True
    # Si llegamos aqui, el producto no existe.
    return False

def agregar_al_carrito(codigo, cantidad):
    # Vemos si existe el producto...
    producto = consultar_producto(codigo)
    # Si se devolvio un falso, el producto no existe.
    if producto is False:
        print("El producto no existe.")
        return False
    # Vemos si hay cantidad suficiente de ese producto...
    if producto['cantidad'] < cantidad:
        print("Cantidad en stock insuficiente.")
        return False
    # Verificar si el producto ya está en el carrito
    for item in carrito:
        if item['codigo'] == codigo:
            # Si existe, sumo a la cantidad del carrito...
            item['cantidad'] += cantidad
            # ...y descuento del stock de ese producto.
            producto['cantidad'] -= cantidad
            return True
    # Si el producto no está en el carrito, se agrega como un nuevo item
    nuevo_item = {
        'codigo': codigo,
        'descripcion': producto['descripcion'],
        'cantidad': cantidad,
        'precio': producto['precio']
    }
    carrito.append(nuevo_item)
    # ...y descuento del stock de ese producto.
    producto['cantidad'] += cantidad
    return True

def quitar_del_carrito(codigo, cantidad):
    # Recorremos la lista de productos en el carrito...
    for item in carrito:
        # Si se ecuentra ese producto...
        if item['codigo'] == codigo:
            # Si no hay cantidad suficiente en el carrito...
            if cantidad > item['cantidad']:
                print("Cantidad a quitar mayor a la cantidad en el carrito.")
                return False
        # Si llegue aqui, es que puedo descontarlos del carrito...
        item['cantidad'] -= cantidad
        # ...y reponerlos en el stock de productos!
        producto = consultar_producto(codigo)
        modificar_producto(codigo, producto["descripcion"], producto["cantidad"]-cantidad, producto["precio"] )

        # Compruebo si la cantidad de ese producto en el carrito es cero:
        if item['cantidad'] == 0:
            # Si quedo en cero, lo elimino del carrito.
            carrito.remove(item)
            return True
        # Si el bucle finaliza sin novedad, es que ese producto NO ESTA en el carrito.
        print("El producto no se encuentra en el carrito.")
        return False

def mostrar_carrito():
    """
    Muestra en pantalla el contenido del carrito de compras.
    """
    # Inicializamos una variable para sumar los importes de cada item
    suma = 0
    print("-"*30)
    # Recorremos la lista de productos en el carrito
    # y mostramos los datos de cada producto.
    for item in carrito:
        print(f'Cod: {item["codigo"]} - {item["descripcion"]}')
        print(f'Precio: {item["precio"]} Cantidad: {item["cantidad"]}')
        # Calculamos el importe a pagar por el producto...
        importe = item["precio"] * item["cantidad"]
        # ...y acumulamos el importe en la variable suma.
        suma += importe
        print(f'Importe: {importe}')
        print("-"*30)
    print(f'Importe TOTAL: {suma}')
    return True