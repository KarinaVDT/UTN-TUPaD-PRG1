# 1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja

notas = []

for i in range(1, 11):
    nota = float(input(f"Ingrese la nota del estudiante {i}: "))
    notas.append(nota)

print("\nNotas registradas:")
for i, n in enumerate(notas, start=1):
    print(f"Estudiante {i}: {n}")

promedio = sum(notas) / len(notas)

nota_max = max(notas)
nota_min = min(notas)

print(f"\nPromedio de notas: {promedio:.2f}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista
productos = []
for i in range(1, 6):
    prod = input(f"Ingrese el producto {i}: ")
    productos.append(prod)
print("\nLista ordenada alfabéticamente:")
for p in sorted(productos):
    print("-", p)
eliminar = input("\nIngrese el producto que desea eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
    print("\nLista actualizada después de eliminar:")
    for p in productos:
        print("-", p)
else:
    print(f"\nEl producto '{eliminar}' no está en la lista.")

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
import random

numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("\nLista generada:")
for i, n in enumerate(numeros, start=1):
    print(f"Num {i}: {n}")
print("\nLista de pares:")
for p in pares:
    print(p, end=" ")
print("\n\nLista de impares:")
for imp in impares:
    print(imp, end=" ")
print(f"\n\nCantidad de pares: {len(pares)}")
print(f"Cantidad de impares: {len(impares)}")

#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

valores = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sin_repetidos = []
for v in valores:
    if v not in sin_repetidos:
        sin_repetidos.append(v)

print("Lista original:")
for i, v in enumerate(valores, start=1):
    print(f"{i}: {v}")

print("\nLista sin repetidos:")
for i, v in enumerate(sin_repetidos, start=1):
    print(f"{i}: {v}")

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

presentes = ["Ana", "Juan", "María", "Pedro", "Agustina", "Sofía", "Constanza", "Ornella"]

print("Lista inicial de presentes:")
for i, nombre in enumerate(presentes, start=1):
    print(f"{i}. {nombre}")

opcion = input("\n¿Querés (A)gregar un nuevo estudiante o (E)liminar uno? [A/E]: ").upper()
if opcion == "A":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    presentes.append(nuevo)
    print(f"\nSe agregó a {nuevo}.")
elif opcion == "E":
    elim = input("Ingrese el nombre del estudiante a eliminar: ")
    if elim in presentes:
        presentes.remove(elim)
        print(f"\nSe eliminó a {elim}.")
    else:
        print(f"\n El estudiante '{elim}' no estaba en la lista.")
else:
    print("\n Opción no válida. No se hicieron cambios.")

print("\nLista final de presentes:")
for i, nombre in enumerate(presentes, start=1):
    print(f"{i}. {nombre}")

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).
numeros = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:")
for i, n in enumerate(numeros, start=1):
    print(f"{i}: {n}")

ultimo = numeros[-1] 
for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1] 
numeros[0] = ultimo  

print("\nLista rotada a la derecha:")
for i, n in enumerate(numeros, start=1):
    print(f"{i}: {n}")

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [10, 20],  
    [12, 22],  
    [9, 18],   
    [14, 25],  
    [11, 19],  
    [13, 24],  
    [8, 21]    
]

print("Temperaturas de la semana (min, max):")
for i, (tmin, tmax) in enumerate(temperaturas, start=1):
    print(f"Día {i}: mínima={tmin}, máxima={tmax}")

minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

print(f"\nPromedio de mínimas: {prom_min:.2f}")
print(f"Promedio de máximas: {prom_max:.2f}")

amplitudes = [fila[1] - fila[0] for fila in temperaturas]
mayor_amp = max(amplitudes)
dia_mayor = amplitudes.index(mayor_amp) + 1

print(f"\nMayor amplitud térmica: {mayor_amp} (Día {dia_mayor})")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],
    [5, 9, 7], 
    [10, 6, 8],
    [4, 7, 5], 
    [9, 8, 10] ]

print("Matriz de notas (estudiantes x materias):")
for i, fila in enumerate(notas, start=1):
    print(f"Estudiante {i}: {fila}")

print("\nPromedio de cada estudiante:")
for i, fila in enumerate(notas, start=1):
    prom = sum(fila) / len(fila)
    print(f"Estudiante {i}: {prom:.2f}")

print("\nPromedio de cada materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    col = [notas[i][j] for i in range(len(notas))]
    prom = sum(col) / len(col)
    print(f"Materia {j+1}: {prom:.2f}")

#9 - Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    print("\nTablero actual:")
    for fila in tablero:
        print(" | ".join(fila))
    print()  

mostrar_tablero()

for turno in range(4):  
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador {jugador}")

    fila = int(input("Ingrese un numero de fila (1-3): ")) - 1
    col  = int(input("Ingrese un numero de columna (1-3): ")) - 1

    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print(" Casilla ocupada, perdés el turno.")

    mostrar_tablero()


# 10 Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.
ventas = [
    [10, 15, 20, 18, 25, 22, 30],
    [5, 8, 12, 10, 9, 14, 11],   
    [20, 22, 18, 24, 30, 28, 25],
    [12, 18, 15, 20, 22, 19, 17] 
]
print("Ventas registradas (productos x días):")
for i, fila in enumerate(ventas, start=1):
    print(f"Producto {i}: {fila}")

print("\nTotal vendido por cada producto:")
totales_producto = []
for i, fila in enumerate(ventas, start=1):
    total = sum(fila)
    totales_producto.append(total)
    print(f"Producto {i}: {total}")

print("\nVentas totales por día:")
totales_dia = []
for j in range(len(ventas[0])):
    col = [ventas[i][j] for i in range(len(ventas))]
    total_dia = sum(col)
    totales_dia.append(total_dia)
    print(f"Día {j+1}: {total_dia}")

dia_max = totales_dia.index(max(totales_dia)) + 1
print(f"\nDía con mayores ventas: Día {dia_max} (Total = {max(totales_dia)})")

prod_max = totales_producto.index(max(totales_producto)) + 1
print(f"Producto más vendido en la semana: Producto {prod_max} (Total = {max(totales_producto)})")
