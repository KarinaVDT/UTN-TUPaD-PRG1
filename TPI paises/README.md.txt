Gestión de Países en Python

Descripción
Este proyecto forma parte del **Trabajo Práctico Integrador (TPI)** de la materia **Programación I** de la **Tecnicatura Universitaria en Programación (UTN)**.  
La aplicación permite **gestionar información sobre países**, aplicando estructuras secuenciales, condicionales y repetitivas, además de conceptos de modularización, funciones, listas, diccionarios y manejo de archivos CSV.

---

Objetivos
- Aplicar los contenidos teóricos de la materia en un proyecto integrador.
- Desarrollar un sistema funcional en Python que lea, procese y gestione datos desde un archivo CSV.
- Implementar búsquedas, filtros, ordenamientos y estadísticas utilizando estructuras de datos adecuadas.
- Practicar el trabajo colaborativo y el uso de GitHub como repositorio de código.

---

Estructura del proyecto

```
tpi-paises/
├─ src/
│  └─ paises.py          Código fuente principal
├─ data/
│  └─ paises.csv         Dataset base de países
├─ docs/
│  ├─ informe.pdf        Informe final en formato APA
│  └─ capturas/          Evidencias y capturas de ejecución
└─ README.md             Archivo de documentación del proyecto
```

---

Requisitos y ejecución

Requisitos:
- Python 3.10 o superior  
- Editor recomendado: Visual Studio Code  

Ejecución:
1. Clonar o descargar el repositorio.  
2. Abrir el proyecto en VS Code.  
3. Ejecutar el archivo principal desde la terminal:
   ```bash
   python src/paises.py
   ```
4. Seguir las opciones del menú para mostrar, buscar, filtrar, ordenar, calcular estadísticas o agregar países.

---
Ejemplos de uso

Buscar país (búsqueda parcial):
```
Término: ar
Resultado:
- Argentina | Pob: 46000000 | Sup: 2780400 km² | América del Sur
```

Filtro por rango de población:
```
Mínimo: 40000000
Máximo: 100000000
Resultado:
- Argentina
- Alemania
```

Estadísticas:
```
País con mayor población: Brasil
País con menor población: Argentina
Promedio de población: 115000000
Promedio de superficie: 2600000 km²
```
 Funcionalidades principales
- Carga de datos desde archivo CSV.  
- Búsqueda exacta y parcial por nombre.  
- Filtros por continente, población o superficie.  
- Ordenamientos por nombre, población o superficie.  
- Cálculo de estadísticas (máximo, mínimo, promedio y conteo por continente).  
- Agregado y actualización de países con validaciones.  
- Menú principal de navegación por consola.

---

Integrantes
- Karina Vanesa D’Angelo
- Jael Vocos

---

Docente y cátedra
Materia: Programación I  
Carrera: Tecnicatura Universitaria en Programación (UTN)  
Coordinador: Alberto Cortez
Docente Comisión 4: Ana Mutti
Docente Comisión 12: Franco Gonzalez
Año: 2025 – 2º Cuatrimestre  

---

Enlaces
- [Informe completo en formato PDF](./docs/informe.pdf)
- [Video presentación del proyecto](https://youtu.be/RBw1icwYbzM)
- [Repositorio GitHub](https://github.com/KarinaVDT/UTN-TUPaD-PRG1/tree/a7eb1143001b96dc97b033d17210954356fb3993/TPI%20paices/src%20-%20Codigo%20fuente)

