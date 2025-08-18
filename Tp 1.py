# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# Ejercicio 4
import math
radio = float(input("Ingrese el radio de un círculo: "))
area = math.pi * (radio)**2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es de {area:.2f} y el perímetro es de {perimetro:.2f}.")

# Ejercicio 5
segundos = float(input("Ingrese la cantidad de segundos a convertir en horas equivalente: "))
horas = round(segundos / 3600, 2)
print(f"El equivalente a {segundos} segundos son {horas} horas.")

# Ejercicio 6
n = int(input("Ingrese un numero para luego mostrar una tabla de multiplicar: "))
print(f"tabla del {n}:")
for i in range(1,10+1):
    print(f"{n} x {i} = {n*i}")

#Ejercicio 7:
n1 = int(input("Ingrese un numero distinto de 0: "))
n2 = int(input("Ingrese un segundo numero distinto de 0:"))
print(f"La suma de {n1} + {n2} = {n1 + n2}")
print(f"la resta de {n1} - {n2} = {n1 - n2}")
print(f"La multiplicacion de {n1} x {n2} = {n1 * n2}")
print(f"La division de {n1} / {n2} = {round(n1 / n2)}")

#Ejercicio 8:
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
print(f"Su indice de masa corporal es: {round(peso/(altura**2))}")

#Ejercicio 9: 
tc = float(input("Ingrese una temperatura en grados Celcius: "))
print(f"El equivalente de la temperatura ingresada en grados Celsius a grados Fahrenheit es: {(9/5*tc + 32):.2f}")

#Ejercicio 10:
n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese un segundo numero: "))
n3 = float(input("Ingrese un tercer numero: "))
print(f"El promedio entre {n1}, {n2} y {n3} = {((n1+n2+n3)/3):.2f}")