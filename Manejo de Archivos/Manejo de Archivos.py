#Ejercicio 1

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,850.0,12\n")
    archivo.write("Marcador,430.0,20\n")

print("Archivo 'productos.txt' creado correctamente.")

#Ejercicio 2
productos = []

try:
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",")
            nombre = partes[0]
            precio = float(partes[1])
            cantidad = int(partes[2])

            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

            
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
except FileNotFoundError:
    print("No existe 'productos.txt'. Primero ejecutá el Punto 1 para crearlo.")

#Ejercicio 3
respuesta = input("\n¿Querés agregar un nuevo producto? (si/no): ")
if respuesta.lower() == "si":
    nombre_nuevo = input("Ingresá el nombre: ")
    precio_nuevo = float(input("Ingresá el precio sin el signo $: "))
    cantidad_nueva = int(input("Ingresá la cantidad: "))

    
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n")

    #Ejercicio 4 
    productos.append({
        "nombre": nombre_nuevo,
        "precio": precio_nuevo,
        "cantidad": cantidad_nueva
    })
    print("Producto agregado.")

#Ejercicio 5
buscado = input("\nIngresá el nombre del producto a buscar: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscado.lower():
        print(f"Encontrado -> Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("No existe un producto con ese nombre.")

#Ejercicio 6
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo 'productos.txt' actualizado con todos los productos.")
