#punto 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#punto 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Tu nombre: ")
print(saludar_usuario(nombre))

#punto 3 informacion_personal(nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

n = input("Nombre: "); a = input("Apellido: ")
e = int(input("Edad: ")); r = input("Residencia: ")
informacion_personal(n, a, e, r)

#punto 4 Área y perímetro del círculo
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

r = float(input("Radio: "))
print("Área:", round(calcular_area_circulo(r), 2))
print("Perímetro:", round(calcular_perimetro_circulo(r), 2))

#punto 5 segundos_a_horas(segundos) → devuelve horas
def segundos_a_horas(segundos):
    return segundos / 3600

s = int(input("Segundos: "))
print("Horas:", round(segundos_a_horas(s), 2))

#punto 6 tabla_multiplicar(numero) (del 1 al 10)
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

n = int(input("Número: "))
tabla_multiplicar(n)

#punto 7 operaciones_basicas(a, b) → devuelve tupla (suma, resta, mult, div)
def operaciones_basicas(a, b):
    division = a / b if b != 0 else None   # evita división por cero
    return (a + b, a - b, a * b, division)

print(operaciones_basicas(12, 3))  # (15, 9, 36, 4.0)

# punto 8 calcular_imc(peso, altura) → devuelve IMC; mostrar con 2 decimales
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

p = float(input("Peso (kg): "))
h = float(input("Altura (m): "))
print(f"IMC: {calcular_imc(p, h):.2f}")

#punto 9 celsius_a_fahrenheit(celsius) → devuelve F
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

c = float(input("°C: "))
print("°F:", celsius_a_fahrenheit(c))

#punto 10 calcular_promedio(a, b, c) → devuelve promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

print(f"Promedio: {calcular_promedio(7, 8, 9):.2f}")
