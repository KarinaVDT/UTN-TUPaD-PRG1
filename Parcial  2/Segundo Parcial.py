"""Segundo parcial de Programacion I - Karina Vanesa D'Angelo"""

import csv
import os

NOMBRE_ARCHIVO = "productos.csv"

def obtenerProductos():
    """Lee el archivo CSV y devuelve una lista de productos como diccionarios. 
  Si el archivo no existe, crea una lista vacia con encabezados"""  
    
    productos = []
   
    #Si el archivo no existe , lo crea con encabezado vacio
    if not os.path.exists(NOMBRE_ARCHIVO): #verifica si existe el archivo csv
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo: #si no existe, abre el archivo con w para crear uno nuevo
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])  #crea el encabezado
            escritor.writeheader() #escribe
            return productos
   
    #Lectura del archivo existente
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo: 
        lector = csv.DictReader(archivo)

        for fila in lector:
            productos.append({"nombre": fila["nombre"], "precio": float(fila["precio"])}) #pasa los numeros a decimales
    
    return productos    


def agregarProducto(producto):
    """Agrega un nuevoproducto al archivo csv 
    Args: producto (dict): es un diccionario con claves, nombre y precio"""

    file_exists = os.path.exists(NOMBRE_ARCHIVO)
    write_header = (not file_exists) or os.path.getsize(NOMBRE_ARCHIVO) == 0

    #append (a), agrega sin borrar datos existentes
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        if write_header:
            escritor.writeheader()
        escritor.writerow(producto)


def existe_producto(nombre): 
    """Verifica si existe un producto con el nombre indicando en el archivo
    
    El argumento es un str, que es el nombre del producto que estamos buscando, 
    y devuelve un booleano (V o F)"""
    
    productos = obtenerProductos() 

    for producto in productos: #recorre todos los productos en busca de coincidencias por nombre
        if producto ["nombre"].lower() == nombre.strip().lower():
            return True
        
    return False

def validar_numero_positivo(precio): #validacion importante, datos ingresados sean numeros positivos y decimales
    if precio.count(".") > 1: #no puede tener mas de un punto decimal (.)
        return False

    if not precio.replace(".", "").isdigit(): #deben ser diginos (formato numerico)
        return False
    return True


def mostrar_productos():
    """Mostrar la lista de productos que estan en el archivo csv"""
    print("----Listado de Productos ---- ")
    
    productos = obtenerProductos()
    
    print("Nombre     Precio")
    
    for producto in productos: #recorre la lista y muestra los productos.
        print(f'{producto["nombre"]} - ${producto["precio"]}')


def agregar_producto():
    """Solicita al usuario los datos de un nuevo producto y los agrega al archivo,
    validando que no exista previamente y que el precio sea valido"""

    print("----AGREGAR NUEVO PRODUCTO----")
    nombre = input("Ingrese nombre: ").strip()

    #validacion, no agregar nombres repetidos
    if existe_producto(nombre):
        print("El producto ya existe")
        return #finaliza la validacion

    precio = input("Ingrese precio: ").strip().replace(",", ".")

    if not validar_numero_positivo(precio):
        print("El precio no es valido")
        return

    precio = float(precio)

    agregarProducto({"nombre": nombre, "precio": precio}) #guarda los cambios realizados
    
    print("Se agrego correctamente el producto")


def guardarProductos(productos):
    """ Guarda una lista completa de productos en el archivo csv,
    pero no conserva el dato anterios del producto que estamos editando"""

    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo: #con el modo W, se sobreescriben los datos
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        escritor.writeheader()
        escritor.writerows(productos)


def editar_producto():
    """Modifica el precio de un producto que ya existe"""

    nombre = input("Ingrese nombre que quiere modificar: ").strip()
    
    if not nombre: #El producto debe existir
        print("El nombre no puede estar vacio")
        return

    productos = obtenerProductos()

    for producto in productos: #busca los productos por nombre
        if producto["nombre"].lower() == nombre.lower():
            precio = input("ingrese nuevo precio: ").strip()

            if not validar_numero_positivo(precio):
                print("El precio no es valido")
                return
            
            producto["precio"] = float(precio) #actualiza el precio vigente

            guardarProductos(productos) #guarda los cambios
          
            print("El producto fue guardado con exito")
            return
    else:
        print("No se encuentra el producto en el archivo.") #si el producto no existe


def Eliminar_producto():
    """Elimina un producto existente del archivo CSV"""

    nombre = input("Ingrese nombre que quiere eliminar: ").strip()
    
    if not nombre: 
        print("El nombre no puede estar vacio")
        return
    
    productos = obtenerProductos()
    productos_filtrado = []

    for producto in productos: #validacion cruzada en la busqueda del producto a eliminar
        if nombre.lower() != producto["nombre"].lower():
            productos_filtrado.append(producto)
    if len(productos_filtrado) == len(productos):
        print("El producto no se encuentra en el archivo")
        return

    guardarProductos(productos_filtrado) #guarda los cambios realizados (actualiza)

    print("EL producto fue eliminado correctamente")



def mostrar_menu(): 
    """menu principal del programa, y permite al usuario 
    seleccionar teniendo a la vista todas las opciones"""
    while True:
        print("="*30)
        print("1. Mostrar productos ")
        print("2. Agregar producto ")
        print("3. Editar precio de producto ")
        print("4. Eliminar producto ")
        print("5. Salir")
        print("="*30)
        opcion = input("ingrese opcion: ").strip()

        match opcion: # match-case se usa para manejar opciones
            case"1":
                mostrar_productos()
            case"2":
                agregar_producto()
            case"3":
                editar_producto()
            case"4":
                Eliminar_producto()
            case"5":
                print("Gracias por usar nuestra aplicaciòn 🙌")
                break
            case _:
                print("La opcion seleccionada no es valida")
mostrar_menu() #entrada principal

        

