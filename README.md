<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:306998,100:FFD43B&height=180&section=header&text=Gestión%20de%20Datos%20de%20Países🐍&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35" />
</p>

---

# 📘 TPI - Programación 1 - UTN

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)  
![Estado](https://img.shields.io/badge/Estado-En%20Progreso-yellow)  
![GitHub repo size](https://img.shields.io/github/repo-size/CTapia10/TPI-Programacion)

---

## 👨‍💻 Autores
- **Nombre:** Daniela Velazquez y Cristian Tapia 
- **Comisión:** 12 y 13  
- **Materia:** Programación 1
- **Profesor:** Ariel Enferrel
- **Tutores:** Franco Gonzalez y Miguel Barrera
- **Universidad:** Universidad Nacional Tecnológica  

---

## 📂 Estructura del repositorio
📦 TPI-Programacion  
 ┣ ...  
 ┣📜 README.md  
 ┣📂 codigo  
   ┗📜 gestion-datos-paises.py  
   ┗📜 dataset.csv  
 
---

## 📚 Descripción del programa

Este proyecto es el Trabajo Práctico Integrador (TPI) de la materia, diseñado para aplicar y consolidar los conceptos fundamentales de la programación aprendidos en la cursada, como listas, diccionarios, funciones y estructuras de control.

El programa es una aplicación de consola desarrollada en **Python 3.10+** que permite gestionar información sobre países. El sistema lee los datos iniciales desde un archivo `dataset.csv` y permite al usuario interactuar con la información a través de un menú de opciones. Los datos se manejan en memoria utilizando **listas** y **diccionarios**.

Cada país en el dataset se representa con la siguiente estructura :
* **Nombre** (string)
* **Población** (int)
* **Superficie en km²** (int)
* **Continente** (string)

### Funcionalidades implementadas

El programa ofrece un menú interactivo con las siguientes funcionalidades, cumpliendo con todos los requisitos mínimos de la consigna:

1.  **Agregar país:** Permite al usuario añadir un nuevo país al dataset. Solicita todos los datos (nombre, población, superficie y continente) y valida que no haya campos vacíos.
2.  **Actualizar población y superficie:** Modifica los datos de población y superficie de un país ya existente, buscándolo por su nombre.
3.  **Buscar un país:** Realiza una búsqueda por nombre. La búsqueda detecta coincidencias parciales o exactas y muestra todos los países que coincidan con el término ingresado.
4.  **Filtrar países:** Ofrece un submenú para filtrar la lista de países por:
    * Continente 
    * Rango de población 
    * Rango de superficie 
5.  **Ordenar países:** Ofrece un submenú para ordenar según el criterio seleccionado por el usuario (El orden puede ser ascendente o descendente):
    * Nombre 
    * Población 
    * Superficie
6.  **Mostrar estadísticas:** Ofrece un submenú para seleccionar y presentar los siguientes indicadores clave del dataset:
    * País con mayor y menor población 
    * Promedio de población 
    * Promedio de superficie 
    * Cantidad de países por continente 
7.  **Salir:** Termina la ejecución del programa.

El script también incluye validaciones de entrada para prevenir errores y mostrar mensajes claros al usuario, conforme a los requisitos de la consigna.

---

## 📌 Instrucciones de uso

### Requisitos previos

* **Python 3.10 o superior**. El código `gestion-datos-paises.py` utiliza la estructura `match-case`, una característica introducida en Python 3.10.

### Configuración

1.  Clona o descarga este repositorio en tu máquina local.
2.  Asegúrate de que el archivo `dataset.csv` se encuentre en la **misma carpeta** que el script `gestion-datos-paises.py` (ambos dentro de la carpeta `codigo/`).
3.  El programa está diseñado para leer el CSV desde su propio directorio de ejecución.

### Ejecución

1.  Abre una terminal o símbolo del sistema.
2.  Navega hasta la carpeta `codigo/` donde se encuentra el script:
    ```bash
    cd ruta/a/TPI-Programacion/codigo
    ```
3.  Ejecuta el script con el siguiente comando:

    ```bash
    python gestion-datos-paises.py
    ```

    (Dependiendo de tu instalación de Python, es posible que necesites usar `python3`):

    ```bash
    python3 gestion-datos-paises.py
    ```

4.  Una vez ejecutado, verás el menú principal en la consola y podrás comenzar a interactuar con el programa ingresando el número de la opción deseada.
---

## 🎯 Ejemplos de entradas y salidas

**Menú Principal**

Al iniciar el programa, se muestra el menú principal:
```
==============================================================
Bienvenido al menu de paises, elija una opción
==============================================================
1. Agregar pais
2. Actualizar poblacion y superficie de un pais
3. Buscar un pais
4. Filtrar paises
5. Ordenar paises
6. Mostrar estadisticas
7. Salir
==============================================================
Opción seleccionada:
```
---
**Ejemplo 1: Buscar un país (Opción 3)**

Se busca un país por coincidencia parcial (ej. "arg"), basado en el `dataset.csv`.
```
Opción seleccionada: 3
==============================================================

Ingrese el nombre: arg
==============================================================
 Paises que coinciden con 'arg':
==============================================================
Pais: Argentina
Poblacion: 46,000,000
Superficie: 2,780,400km²
Continente: America del Sur
==============================================================
```
---
**Ejemplo 2: Mostrar Estadísticas (Opción 6 -> 4)**

Se muestra la cantidad de países por continente, basado en el `dataset.csv`.
```
Opción seleccionada: 6
==============================================================
 Elija una opción
==============================================================
1. Pais con mayor y menor poblacion
2. Promedio de Poblacion
3. Promedio de Superficie
4. Cantidad de paises por continente
5. Volver al menu principal
==============================================================
Opción seleccionada: 4
==============================================================

==============================================================
✅ Paises del dataset dentro del continente 'Asia'
==============================================================
Pais: China
Poblacion: 1,425,000,000
Superficie: 9,596,961km²
Continente: Asia
==============================================================
Pais: India
Poblacion: 1,417,000,000
Superficie: 3,287,263km²
Continente: Asia
==============================================================
Pais: Japon
Poblacion: 125,000,000
Superficie: 377,975km²
Continente: Asia
==============================================================
Total: 3 pais/es
==============================================================
```
(Salida similar para America del Norte, Africa, America del Sur, Europa y Oceania)

---
**Ejemplo 3: Mensaje de error (Opción inválida)**

Al ingresar una opción no válida en el menú principal.
```
Opción seleccionada: 9
==============================================================
⚠️  Opción inválida. Por favor, elija una opción del 1 al 7.
```
---

## Diagrama de Estructura Modular

```mermaid
graph TD
    subgraph A[PROGRAMA PRINCIPAL]
        P(programa_principal: Muestra el Menú)
    end
    P --> L1
    P --> L2
    P --> L3
    L1 --> U1
    L1 --> D1
    L1 --> D2
    L2 --> U1
    L2 --> D1
    L2 --> D2
    L3 --> D1
    L3 --> U1
    D1 -.-> CSV[Archivo dataset.csv]
    D2 -.-> CSV

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFD43B,100:306998&height=120&section=footer"/>
</p>
