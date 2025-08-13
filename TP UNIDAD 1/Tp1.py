>>> # Ejercicio 1
... print("Hola Mundo!")
... # Ejercicio 2
... nombre = input("Por favor, ingrese su nombre: ")
... print(f"Hola {nombre}!")
... print("Hola " + nombre + "!")
... # Ejercicio 3
... nombre = input("Por favor, ingrese su nombre: ")
... apellido = input("Por favor, ingrese su apellido: ")
... edad = input("Por favor, ingrese su edad: ")
... lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")
... print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")
... # Ejercicio 4
... import math
... radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))
... area_circulo = math.pi * (radio_circulo)**2
... perimetro_circulo = 2 * math.pi * radio_circulo
... print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")
... import math
... radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))
... area_circulo = round(math.pi * (radio_circulo)**2, 2)
... perimetro_circulo = round(2 * math.pi * radio_circulo, 2)
... print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")
...
... # Ejercicio 5
... cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))
... cantidad_horas = round(cantidad_segundos / 3600, 2)
... print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas.")
...
... # Ejercicio 6
