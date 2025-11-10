 
"""
==================================================
        TPI - PROGRAMACION I
==================================================
Tema: Gestion de Datos de Países (CSV)
Integrantes: Karina Vanesa D'Angelo y Jael Vocos
"""

import csv
import os

NOMBRE_CSV = "paises.csv"  # archivo base esperado en el mismo directorio

def normalizar_texto(t):
    """
    Normaliza un texto para comparaciones:
    - elimina espacios extremos
    - comprime espacios intermedios
    - pasa a minúsculas
    """
    t = t.strip()
    t = " ".join(t.split())
    return t.lower()

def es_entero_no_negativo(txt):
    """
    Verifica si txt representa un entero >= 0
    """
    txt = txt.strip()
    return txt.isdigit()

def es_entero_positivo(txt): 
    """
    Verifica si txt representa un entero > 0
    """
    if not es_entero_no_negativo(txt):
        return False
    return int(txt) > 0

def leer_entero_no_negativo(msj):
    """
    Lee por input un entero >= 0 
    """
    while True:
        s = input(msj).strip()
        if es_entero_no_negativo(s):
            return int(s)
        print("Error: ingrese un entero mayor o igual a 0.")

def leer_entero_positivo(msj):
    """
    Lee por input un entero > 0
    """
    while True:
        s = input(msj).strip()
        if es_entero_positivo(s):
            return int(s)
        print("Error: ingrese un entero mayor a 0.")

def leer_texto_no_vacio(msj):
    """
    Lee texto no vacío.
    """
    while True:
        s = input(msj).strip()
        if s != "":
            return " ".join(s.split())  # compacta espacios
        print("Error: el texto no puede estar vacío.")

def cargar_paises(nombre_archivo):
    """
    Lee el CSV (si existe) y construye la lista de países (lista de dicts).
    Cada dict tiene: nombre (str), poblacion (int), superficie (int), continente (str).
    """
    paises = []
    if not os.path.exists(nombre_archivo):
        return paises  # empieza vacío si no existe

    with open(nombre_archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        # Se espera encabezado con: nombre,poblacion,superficie,continente
        # Validación simple de headers
        headers = lector.fieldnames if lector.fieldnames is not None else []
        headers_norm = [ (h or "").strip().lower() for h in headers ]
        requeridos = ["nombre","poblacion","superficie","continente"]
        faltan = False
        for req in requeridos:
            if req not in headers_norm:
                faltan = True
        if faltan:
            print("Aviso: El CSV no posee los encabezados requeridos (nombre,poblacion,superficie,continente). Se ignora el archivo.")
            return []

        # Lectura segura sin excepciones
        for fila in lector:
            # Normalización de claves (por si vienen con mayúsculas)
            nombre = (fila.get("nombre") or fila.get("NOMBRE") or "").strip()
            poblacion_txt = (fila.get("poblacion") or fila.get("POBLACION") or "").strip()
            superficie_txt = (fila.get("superficie") or fila.get("SUPERFICIE") or "").strip()
            continente = (fila.get("continente") or fila.get("CONTINENTE") or "").strip()

            if nombre == "" or continente == "":
                # fila inválida por campos vacíos
                continue
            if not (es_entero_no_negativo(poblacion_txt) and es_entero_positivo(superficie_txt)):
                # números inválidos
                continue

            paises.append({
                "nombre": " ".join(nombre.split()),
                "poblacion": int(poblacion_txt),
                "superficie": int(superficie_txt),
                "continente": " ".join(continente.split())
            })
    return paises

def guardar_paises(nombre_archivo, paises):
    """
    Persiste la lista completa en CSV (reescribe todo).
    """
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for p in paises:
            escritor.writerow({
                "nombre": p["nombre"],
                "poblacion": p["poblacion"],
                "superficie": p["superficie"],
                "continente": p["continente"],
            })

def buscar_indice_por_nombre(paises, nombre_objetivo):
    """
    Devuelve el índice del país cuyo nombre coincide exactamente (ignorando mayúsculas y espacios extra).
    Si no existe, retorna -1.
    """
    objetivo = normalizar_texto(nombre_objetivo)
    for i, p in enumerate(paises):
        if normalizar_texto(p["nombre"]) == objetivo:
            return i
    return -1

def agregar_pais(paises, nombre_archivo):
    print("\n=== Agregar pais ===")
    nombre = leer_texto_no_vacio("Nombre: ")
    if buscar_indice_por_nombre(paises, nombre) != -1:
        print("El pais ya existe.")
        return
    continente = leer_texto_no_vacio("Continente: ")
    poblacion = leer_entero_no_negativo("Poblacion (>= 0): ")
    superficie = leer_entero_positivo("Superficie en km 2 (> 0): ")

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    guardar_paises(nombre_archivo, paises)
    print("Pais agregado y guardado.")

def actualizar_pais(paises, nombre_archivo):
    print("\n=== Actualizar datos de un pais ===")
    nombre = leer_texto_no_vacio("Nombre EXACTO del pais a actualizar: ")
    idx = buscar_indice_por_nombre(paises, nombre)
    if idx == -1:
        print("No se encontro el pais.")
        return
    print(f"Actual: poblacion {paises[idx]['poblacion']} | superficie {paises[idx]['superficie']} km2")
    paises[idx]["poblacion"] = leer_entero_no_negativo("Nueva poblacion (>= 0): ")
    paises[idx]["superficie"] = leer_entero_positivo("Nueva superficie (> 0): ")
    guardar_paises(nombre_archivo, paises)
    print("Datos actualizados y guardados.")

def mostrar_todos(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return
    print("\n=== LISTADO COMPLETO ===")
    for p in paises:
        print(f"- {p['nombre']} | Pob: {p['poblacion']} | Sup: {p['superficie']} km2 | {p['continente']}")

def buscar_por_nombre(paises): # Filtros
    print("\n=== Busqueda por nombre ===")
    termino = leer_texto_no_vacio("Ingrese termino: ")
    modo = input("1) Coincidencia parcial  2) Coincidencia exacta -> ").strip()
    resultado = []
    t_norm = normalizar_texto(termino)

    for p in paises:
        nombre_norm = normalizar_texto(p["nombre"])
        if (modo == "2" and nombre_norm == t_norm) or (modo != "2" and t_norm in nombre_norm):
            resultado.append(p)

    if len(resultado) == 0:
        print("Sin resultados.")
    else:
        mostrar_todos(resultado)

def filtrar_paises(paises):
    while True:
        print("\n=== Filtros ===")
        print("1) Por continente")
        print("2) Por rango de poblacion")
        print("3) Por rango de superficie")
        print("4) Volver")
        op = input("Opcion: ").strip()

        if op == "1":
            c = leer_texto_no_vacio("Continente: ").lower()
            res = []
            for p in paises:
                if p["continente"].lower() == c:
                    res.append(p)
            if len(res) == 0:
                print("Sin resultados para ese continente.")
            else:
                mostrar_todos(res)

        elif op == "2":
            print("Enter vacio = sin limite")
            mn_txt = input("Poblacion minima: ").strip()
            mx_txt = input("Poblacion maxima: ").strip()
            mn = int(mn_txt) if es_entero_no_negativo(mn_txt) else None
            mx = int(mx_txt) if es_entero_no_negativo(mx_txt) else None
            if mn is not None and mx is not None and mn > mx:
                print("Rango invalido (min>max)."); continue
            res = []
            for p in paises:
                ok_min = (mn is None) or (p["poblacion"] >= mn)
                ok_max = (mx is None) or (p["poblacion"] <= mx)
                if ok_min and ok_max:
                    res.append(p)
            if len(res) == 0:
                print("Sin resultados para ese rango de poblacion.")
            else:
                mostrar_todos(res)

        elif op == "3":
            print("Enter vacio = sin limite")
            mn_txt = input("Superficie minima: ").strip()
            mx_txt = input("Superficie maxima: ").strip()
            mn = int(mn_txt) if es_entero_no_negativo(mn_txt) else None
            mx = int(mx_txt) if es_entero_no_negativo(mx_txt) else None
            if mn is not None and mx is not None and mn > mx:
                print("Rango invalido (min>max)."); continue
            res = []
            for p in paises:
                ok_min = (mn is None) or (p["superficie"] >= mn)
                ok_max = (mx is None) or (p["superficie"] <= mx)
                if ok_min and ok_max:
                    res.append(p)
            if len(res) == 0:
                print("Sin resultados para ese rango de superficie.")
            else:
                mostrar_todos(res)

        elif op == "4":
            return
        else:
            print("Opcion invalida.")

def comparar_texto_ci(a, b):
    """
    Devuelve True si a <= b en orden alfabetico, ignorando mayusculas.
    """
    A = normalizar_texto(a)
    B = normalizar_texto(b)
    if A < B: 
        return True
    if A == B:
        return True
    return False

def insercion_por_clave(paises, clave, modo="asc"):
    """
    Insertion sort que retorna una nueva lista ordenada por 'clave'.
    - Para 'nombre': orden alfabetico de la A a la Z 
    - Para 'poblacion'/'superficie': asc o desc (numerico)
    """
    ordenados = []
    for x in paises:
        j = len(ordenados) - 1
        if clave == "nombre":
            while j >= 0 and not comparar_texto_ci(ordenados[j]["nombre"], x["nombre"]):
                j -= 1
        else:
            if modo == "asc":
                while j >= 0 and ordenados[j][clave] > x[clave]:
                    j -= 1
            else:  # desc
                while j >= 0 and ordenados[j][clave] < x[clave]:
                    j -= 1
        ordenados.insert(j + 1, x)
    return ordenados

def ordenar_paises(paises):
    while True:
        print("\n=== Ordenar ===")
        print("1) Por nombre (A - Z)")
        print("2) Por poblacion (ascendente)")
        print("3) Por superficie (ascendente/descendente)")
        print("4) Volver")
        op = input("Opcion: ").strip()

        if op == "1":
            mostrar_todos(insercion_por_clave(paises, "nombre", "asc"))
        elif op == "2":
            mostrar_todos(insercion_por_clave(paises, "poblacion", "asc"))
        elif op == "3":
            modo = input("Ingrese 'asc' o 'desc': ").strip().lower()
            if modo not in ("asc","desc"):
                print("Modo invalido."); continue
            mostrar_todos(insercion_por_clave(paises, "superficie", modo))
        elif op == "4":
            return
        else:
            print("Opcion invalida.")

def estadisticas(paises):
    print("\n=== Estadisticas ===")
    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    # mayor/menor poblacion
    idx_max = 0
    idx_min = 0
    i = 1
    while i < len(paises):
        if paises[i]["poblacion"] > paises[idx_max]["poblacion"]:
            idx_max = i
        if paises[i]["poblacion"] < paises[idx_min]["poblacion"]:
            idx_min = i
        i += 1
    mayor = paises[idx_max]
    menor = paises[idx_min]

    # promedios
    suma_pobl = 0
    suma_sup = 0
    for p in paises:
        suma_pobl += p["poblacion"]
        suma_sup += p["superficie"]
    prom_pobl = suma_pobl / len(paises)
    prom_sup = suma_sup / len(paises)

    # cantidad por continente
    conteo = {}
    for p in paises:
        cont = p["continente"]
        if cont in conteo:
            conteo[cont] += 1
        else:
            conteo[cont] = 1

    print(f"Pais con mayor poblacion: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"Pais con menor poblacion: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de poblacion: {prom_pobl:.2f}")
    print(f"Promedio de superficie: {prom_sup:.2f} km2")
    print("Cantidad de paises por continente:")
    for cont, cant in conteo.items():
        print(f"  - {cont}: {cant}")

def menu():
    paises = cargar_paises(NOMBRE_CSV)

    while True:
        print("\n" + "=" * 45)
        print(" SISTEMA DE PAISES - TPI PROGRAMACION I ")
        print("=" *45 )
        print("1. Agregar pais")
        print("2. Actualizar Poblacion y Superficie de un pais")
        print("3. Buscar pais por nombre (parcial/exacta)")
        print("4. Filtros (continente / rango poblacion / rango superficie)")
        print("5. Ordenar (nombre / poblacion / superficie asc/desc)")
        print("6. Estadisticas")
        print("7. Mostrar todos")
        print("8. Salir")
        print("-" * 45)

        opcion = input("Elija una opcion: ").strip()

        # Estructura de control clara (sin lambdas)
        if opcion == "1":
            agregar_pais(paises, NOMBRE_CSV)
        elif opcion == "2":
            actualizar_pais(paises, NOMBRE_CSV)
        elif opcion == "3":
            buscar_por_nombre(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            estadisticas(paises)
        elif opcion == "7":
            mostrar_todos(paises)
        elif opcion == "8":
            print("Fin del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
