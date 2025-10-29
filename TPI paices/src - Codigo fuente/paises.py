#TRABAJO PRACTICO INTEGRADOR- PROGRAMACION
#Integrantes: Karina D'Angelo y Jael Vocos


#importamos el modulo csv para poder leer archivos csv
import csv

#Define una función para leer números enteros desde teclado, con validaciones
def leer_entero(msj, minimo=None, mayor_que=None, permitir_vacio=False):
    #Bucle para reintentar hasta que el usuario ingrese un valor válido
    while True:
        s = input(msj).strip() #Pide el dato y le quita espacios a los extremos
        #Si se permite vacío y el usuario presiona Enter, devuelve None
        if permitir_vacio and s == "":
            return None
        try:
            n = int(s) #Intenta convertir la cadena a entero.
            #Si se pidió un mínimo y no se cumple, avisa y vuelve a pedir
            if minimo is not None and n < minimo:
                print(f"Error: debe ser >= {minimo}."); continue
            #si se pidio mayor_que y no se cumple, avisa y reintenta
            if mayor_que is not None and n <= mayor_que:
                print(f"Error: debe ser > {mayor_que}."); continue
            return n #si esta todo bien devuelve el entero
        #Si int(s) falla (no es número), muestra error y reintenta
        except ValueError:
            print("Error: ingrese un número entero válido.")

#Define una función para leer texto no vacío.
def leer_texto_no_vacio(msj):
    while True: #creamos un bulce que repite hasta que sea valido
        s = input(msj).strip() #pide y recorta espacios
        #si no esta vacio, lo devuelve
        if s != "":
            return s
        print("Error: no puede estar vacío.") #si estaba vacio, avisa y vuelve a intentar


#Define la función que lee el CSV y devuelve una lista de diccionarios
def cargar_paises_desde_csv(ruta="../data/paises.csv"):
    paises = [] #lista vacia donde se van agregando los paisese
    #Intenta abrir el archivo paises.csv en UTF-8
    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            r = csv.DictReader(f) #Usa DictReader para leer cada fila como diccionario
            #Conjunto con los encabezados obligatorios
            requeridos = {"nombre","poblacion","superficie","continente"}
            #Verifica que el CSV tenga esos encabezados; si no, informa error y retorna lista vacía
            if not r.fieldnames or not requeridos.issubset({h.lower() for h in r.fieldnames}):
                print("Error: el CSV debe tener encabezados: nombre,poblacion,superficie,continente")
                return []
            #Recorre las filas del CSV
            for i, fila in enumerate(r, start=2):
                #Normaliza: claves en minúscula, valores sin espacios y sin None
                fila = {k.lower(): (v or "").strip() for k, v in fila.items()}
                #Extrae y convierte los campos numéricos a int
                try:
                    nombre = fila["nombre"]
                    continente = fila["continente"]
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])
                    #Valida datos mínimos y, si están bien, agrega el país a la lista
                    if nombre and continente and poblacion >= 0 and superficie > 0:
                        paises.append({
                            "nombre": nombre,
                            "poblacion": poblacion,
                            "superficie": superficie,
                            "continente": continente
                        })
                    #Si falló la validación, avisa y no carga esa fila
                    else:
                        print(f"Aviso: fila {i} ignorada por datos inválidos.")
                #Si falló la conversión/parsing, avisa y sigue con la siguiente fila
                except Exception:
                    print(f"Aviso: fila {i} ignorada por formato.")
    #Si el archivo no existe, avisa y no corta el programa
    except FileNotFoundError:
        print(f"Aviso: no se encontró '{ruta}'. Podés cargar países manualmente desde el menú.")
    return paises #Devuelve la lista de países cargados

#creamos una funcion para imprimir una lista de paises
def mostrar(paises):
    #Si la lista está vacía, informa y termina
    if not paises:
        print("Sin resultados.")
        return
    #Recorre e imprime cada país en una sola línea
    for p in paises:
        print(f"- {p['nombre']} | Pob: {p['poblacion']} | Sup: {p['superficie']} km² | {p['continente']}")

#Función para agregar un nuevo país a la lista
def agregar(paises):
    print("\n=== Agregar país ===")
    #Pide textos no vacíos
    nombre = leer_texto_no_vacio("Nombre: ")
    continente = leer_texto_no_vacio("Continente: ")
    #Pide enteros con validación de rango
    poblacion = leer_entero("Población (>=0): ", minimo=0)
    superficie = leer_entero("Superficie en km² (>0): ", mayor_que=0)
    #Crea el diccionario del país y lo agrega a la lista
    paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
    print("País agregado.")

#Función para modificar población y superficie de un país existente
def actualizar(paises):
    #Si no hay datos, avisa y vuelve.
    if not paises:
        print("No hay países cargados."); return
    print("\n=== Actualizar país ===")
    #Pide el nombre exacto (case-insensitive) del país a actualizar.
    objetivo = leer_texto_no_vacio("Nombre EXACTO: ").lower()
    #Busca ese país en la lista.
    for p in paises:
        if p["nombre"].lower() == objetivo:
            #Muestra datos actuales para referencia
            print(f"Actual: Pob {p['poblacion']} | Sup {p['superficie']} km²")
            #Lee y valida los nuevos valores
            p["poblacion"] = leer_entero("Nueva población (>=0): ", minimo=0)
            p["superficie"] = leer_entero("Nueva superficie (>0): ", mayor_que=0)
            print("Actualizado.")
            return
    print("No se encontró el país.")

#Función para buscar países por nombre
def buscar_por_nombre(paises):
    print("\n=== Búsqueda por nombre ===")
    #Pide el texto a buscar (no vacío), en minúsculas
    termino = leer_texto_no_vacio("Término: ").lower()
    #Pregunta si la coincidencia será parcial o exacta
    modo = input("1) Parcial  2) Exacta -> ").strip()
    #Arma la lista de resultados según el modo
    if modo == "2":
        res = [p for p in paises if p["nombre"].lower() == termino]
    else:
        res = [p for p in paises if termino in p["nombre"].lower()]
    mostrar(res)

#Menú de filtros.
def filtros(paises):
    #Permite aplicar varios filtros seguidos hasta Volver
    while True:
        print("\n=== Filtros ===")
        print("1) Por continente")
        print("2) Por rango de población")
        print("3) Por rango de superficie")
        print("4) Volver")
        #Lee opción del usuario
        op = input("Opción: ").strip()
        #Filtro por continente exacto
        if op == "1":
            c = leer_texto_no_vacio("Continente: ").lower()
            mostrar([p for p in paises if p["continente"].lower() == c])
        #Pide rango de población; Enter vacío significa sin límite
        elif op == "2":
            print("Enter vacío = sin límite.")
            mn = leer_entero("Pob mín: ", permitir_vacio=True)
            mx = leer_entero("Pob máx: ", permitir_vacio=True)
            #Valida que mínimo ≤ máximo si ambos existen
            if mn is not None and mx is not None and mn > mx:
                print("Rango inválido."); continue
            #Aplica el filtro y muestra resultados.
            mostrar([p for p in paises if (mn is None or p["poblacion"] >= mn) and (mx is None or p["poblacion"] <= mx)])
        #Análogo al filtro anterior pero con superficie
        elif op == "3":
            print("Enter vacío = sin límite.")
            mn = leer_entero("Sup mín: ", permitir_vacio=True)
            mx = leer_entero("Sup máx: ", permitir_vacio=True)
            #Valida el rango
            if mn is not None and mx is not None and mn > mx:
                print("Rango inválido."); continue
            mostrar([p for p in paises if (mn is None or p["superficie"] >= mn) and (mx is None or p["superficie"] <= mx)])
        #Vuelve al menú anterior
        elif op == "4":
            return
        else:
            print("Opción inválida.")


#Menú de ordenamientos
def ordenar(paises):
    #Muestra opciones y lee la elegida
    while True:
        print("\n=== Ordenar ===")
        print("1) Por nombre (A→Z)")
        print("2) Por población (asc)")
        print("3) Por superficie (asc/desc)")
        print("4) Volver")
        op = input("Opción: ").strip()
        #Ordena por nombre A-Z y muestra
        if op == "1":
            mostrar(sorted(paises, key=lambda x: x["nombre"].lower() ))
        #Ordena por población y muestra
        elif op == "2":
            mostrar(sorted(paises, key=lambda x: x["poblacion"]))
        #Ordena por superficie asc/desc según lo que ingrese el usuario
        elif op == "3":
            modo = input("asc/desc: ").strip().lower()
            mostrar(sorted(paises, key=lambda x: x["superficie"], reverse=(modo=="desc")))
        #Vuelve al menu
        elif op == "4":
            return
        else:
            print("Opción inválida.")


#Calcula y muestra indicadores
def estadisticas(paises):
    print("\n=== Estadísticas ===")
    #Si no hay datos, informa y vuelve
    if not paises:
        print("Sin datos."); return
    #Mayor y menor población
    mx = max(paises, key=lambda x: x["poblacion"])
    mn = min(paises, key=lambda x: x["poblacion"])
    #Promedios de población y superficie
    prom_p = sum(p["poblacion"] for p in paises) / len(paises)
    prom_s = sum(p["superficie"] for p in paises) / len(paises)
    #Conteo de países por continente (diccionario acumulador)
    por_cont = {}
    for p in paises:
        c = p["continente"]
        por_cont[c] = por_cont.get(c, 0) + 1
    print(f"Mayor población: {mx['nombre']} ({mx['poblacion']})")
    print(f"Menor población: {mn['nombre']} ({mn['poblacion']})")
    print(f"Promedio población: {prom_p:.2f}")
    print(f"Promedio superficie: {prom_s:.2f} km²")
    print("Países por continente:")
    #Lista cada continente y su cantidad
    for c, cant in por_cont.items():
        print(f"  - {c}: {cant}")

#Función principal que orquesta la app
def main():
    print("  Gestión de Países (CSV -> Menú)   ")
    #Carga los países desde el archivo CSV
    paises = cargar_paises_desde_csv("paises.csv")
    #Bucle del menú principal. Y muestra las opciones del menu
    while True:
        print("\n===== MENÚ =====")
        print("1) Agregar")
        print("2) Actualizar (población/superficie)")
        print("3) Buscar por nombre")
        print("4) Filtros")
        print("5) Ordenar")
        print("6) Estadísticas")
        print("7) Mostrar todos")
        print("8) Salir")
        op = input("Opción: ").strip()
        #Despacha a la función correspondiente según la opción
        if   op == "1": agregar(paises)
        elif op == "2": actualizar(paises)
        elif op == "3": buscar_por_nombre(paises)
        elif op == "4": filtros(paises)
        elif op == "5": ordenar(paises)
        elif op == "6": estadisticas(paises)
        elif op == "7": mostrar(paises)
        elif op == "8": print("Fin."); break
        else: print("Opción inválida.")
    
#Punto de entrada,si ejecutás este archivo directamente, llama a main()
if __name__ == "__main__":
    main()
