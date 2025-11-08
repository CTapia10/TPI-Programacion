# Programacion 1 | Trabajo Practico Integrador | 2025
# # Daniela Velazquez y Cristian Tapia

# Desarrollar una aplicación en Python que permita gestionar información sobre países,
# aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas,
# ordenamientos y estadísticas. El sistema debe ser capaz de leer datos desde un archivo CSV,
# realizar consultas y generar indicadores clave a partir del dataset

# Cada país estará representado con los siguientes datos:
# • Nombre (string)
# • Población (int)
# • Superficie en km² (int)
# • Continente (string) 

# Ejemplo de registro CSV:
# nombre,poblacion,superficie,continente
# Argentina,45376763,2780400,América
# Japón,125800000,377975,Asia
# Brasil,213993437,8515767,América
# Alemania,83149300,357022,Europa 

# TODO:
# El programa debe ofrecer un menú de opciones en consola que permita:
#   1• Agregar un país con todos los datos necesarios para almacenarse (No se
#   permiten campos vacios).
#   2• Actualizar los datos de Población y Superfice de un Pais.
#   3• Buscar un país por nombre (coincidencia parcial o exacta).
#   4• Filtrar países por:
#       o Continente
#       o Rango de población
#       o Rango de superficie
#   5• Ordenar países por:
#       o Nombre
#       o Población
#       o Superficie (ascendente o descendente)
#   6• Mostrar estadísticas:
#       o País con mayor y menor población
#       o Promedio de población
#       o Promedio de superficie
#       o Cantidad de países por continente
# 3. Validaciones
#   • Controlar errores de formato en el CSV.
#   • Evitar fallos al ingresar filtros inválidos o búsquedas sin resultados.
#   • Mensajes claros de éxito/error. 

#=============================================================================#
#======================== Defino el programa principal =======================#
#=============================================================================#
def programa_principal():
    import csv
    import os
    def Archivo():
        # Guardo el nombre del archivo en variable para reutilizarlo o cambiarlo en todas las coincidencias
        NOMBRE_ARCHIVO = "dataset.csv"
        return NOMBRE_ARCHIVO
    
    def DirArchivo():
        # Ruta absoluta del archivo dataset.csv en la misma carpeta que este script
        base = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(base, Archivo())
        return archivo

    # Defino metodo para verificar si existe el archivo
    def ExisteArchivo(archivo):
        return os.path.isfile(archivo)
    
    def PedirContinente():
        continentes = [ "1. Asia",
                    "2. Africa",
                    "3. America del Norte",
                    "4. America del Sur",
                    "5. Antartida",
                    "6. Europa",
                    "7. Oceania" ]
        while True:
        # Mostramos las opciones del menu al usuario
            print("\n"+"="*54)
            print("Continentes:") 
            print("="*54)
            for opcion in continentes:
                print(opcion)
            print("="*54)
            # Pedimos al usuario que seleccione una de las opciones
            seleccion = input("Opción seleccionada: ").strip()
            print("="*54)
            match seleccion:    
                case "1":
                    continente = "Asia"
                    break
                case "2":
                    continente = "Africa"
                    break
                case "3":
                    continente = "America del Norte"
                    break
                case "4":
                    continente = "America del Sur"
                    break
                case "5":
                    continente = "Antartida"
                    break
                case "6":
                    continente = "Europa"
                    break
                case "7":
                    continente = "Oceania"
                    break
                # Opcion inválida
                case _:
                    print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 7.\n")
                    continue    
        return continente   
    
    # Defino metodo para pedir el nombre del pais o continente al usuario
    def PedirNombre():
        while True:
            nombre = input("\nIngrese el nombre: ").strip().title()
            if not nombre.replace(" ", "").isalpha():
                print(f"\n⚠️  El nombre no debe estar vacio y debe estar formado por letras.")
                continue
            if len(nombre) < 2:
                print(f"\n⚠️  El nombre es demasiado corto.")
                continue
            if len(nombre) > 40:
                print(f"\n⚠️  El nombre es demasiado largo.")
                continue
            return nombre

    # Defino metodo para pedir la cantidad y devolverla sin errores de entrada
    def PedirCantidad():
        while True:
            cantidad = input("\nIngrese la cantidad: ").strip()
            if not cantidad.isdigit():
                print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).")
                continue
            # Despues de verificar que no hayan signos especiales transformo a entero
            cantidad = int(cantidad)
            if not (0 < cantidad):
                print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).")
                continue
            break
        return cantidad
    
    # Defino metodo para persistir los cambios en el archivo csv
    def PersistirCsv(filas_dataset):
        dir_archivo = DirArchivo()
        with open(dir_archivo, "w", newline="", encoding="utf-8") as archivo:
            filas = csv.DictWriter(archivo, fieldnames=["NOMBRE","POBLACION","SUPERFICIE","CONTINENTE"])
            filas.writeheader()
            filas.writerows(filas_dataset)
        return

    # Defino metodo para verificar si un pais existe
    def ExistePais(nombre):
        # Verifica si existe un pais con el nombre indicado en el archivo.
        paises = ObtenerPaises()
        for pais in paises:
            if pais["NOMBRE"] == nombre:
                return True
        return False

    # Defino metodo para obtener paises, en caso que no existan crea un nuevo archivo vacio
    def ObtenerPaises():
        dir_archivo = DirArchivo()
        paises = []
    # Si el archivo no existe, lo crea con encabezado vacío
        if not ExisteArchivo(dir_archivo):
            with open(dir_archivo, "w", newline="", encoding="utf-8") as archivo:
                filas = csv.DictWriter(archivo, fieldnames=["NOMBRE","POBLACION","SUPERFICIE","CONTINENTE"])
                filas.writeheader()
                return paises
        
        with open(dir_archivo, "r", newline="",encoding="utf-8") as archivo:
            filas = csv.DictReader(archivo)
            for fila in filas:
                paises.append({"NOMBRE": fila["NOMBRE"], "POBLACION": int(fila["POBLACION"]), "SUPERFICIE": int(fila["SUPERFICIE"]),"CONTINENTE": fila["CONTINENTE"]})
        return paises


    # Defino metodo para agregar paises al csv sin sobreescribir
    def AgregarPais():
        dir_archivo = DirArchivo()
        while True:
            # Pido al usuario nombre de pais, poblacion, superficie y continente para agregarlo al dataset
            print("\nQue pais desea agregar?")
            nombre_pais = PedirNombre()
            if not ExistePais(nombre_pais):
                print(f"\nCuanta poblacion tiene {nombre_pais}?")
                poblacion = PedirCantidad()
                print(f"\nCuanto tiene de superficie (km²) {nombre_pais}?")
                superficie = PedirCantidad()
                print(f"\nIndique el continente donde se encuentra {nombre_pais}")
                continente = PedirContinente()
                # Agrego al archivo csv el nuevo pais con sus caracteristicas
                with open(dir_archivo, "a", newline="", encoding="utf-8") as archivo:
                    filas = csv.DictWriter(archivo, fieldnames=["NOMBRE", "POBLACION","SUPERFICIE", "CONTINENTE"])
                    filas.writerow({"NOMBRE": nombre_pais, "POBLACION": poblacion,"SUPERFICIE": superficie, "CONTINENTE": continente})
                print(f"\n ✅ Pais {nombre_pais} del continente {continente} con poblacion de {poblacion} personas y superficie de {superficie}km² agregado correctamente.")
                break
            else:
                print(f"\n ⚠️  El pais {nombre_pais} ya se encuentra dentro del dataset.")
                continue
        return

    # Defino metodo para actualizar poblacion y superficie de un pais indicado
    def ActualizarDatos():
        paises = ObtenerPaises()
        if paises:
            print("\nA que pais desea actualizarle su poblacion y superficie?")
            nombre = PedirNombre()
            if ExistePais(nombre):
                for pais in paises:
                    if pais["NOMBRE"] == nombre:
                        print(f"\nIndique la poblacion nueva del pais '{nombre}'")
                        poblacion = PedirCantidad()
                        # Actualizo poblacion
                        pais["POBLACION"] = poblacion
                        print(f"\nIndique la superficie (km²) nueva del pais '{nombre}'")
                        superficie = PedirCantidad()
                        # Actualizo superficie
                        pais["SUPERFICIE"] = superficie
                        print(f"\n ✅ Se modifico con exito la poblacion y superficie del pais '{nombre}' | Poblacion actual: {pais["POBLACION"]}, Superficie actual: {pais["SUPERFICIE"]}km².")
                        PersistirCsv(paises)
                        break
            else:
                print(f"\n ⚠️  El pais '{nombre}' no se encuentra dentro del dataset.")
        else:
            print("\n ⚠️  No hay paises disponibles dentro del dataset.")
        return
    
    # Defino metodo para consultar por un pais en especifico y lo muestro en pantalla
    def BuscarPais():
        paises = ObtenerPaises()
        if not paises:
            print("\n ⚠️  No hay paises disponibles dentro del dataset.\n")
            # Salimos de la función si no hay países
            return  
        pais_busqueda = PedirNombre().lower()
        # Creo variable encontrado para detectar si se encontro alguna coincidencia
        encontrado = False 
        # Tabla con paises que coinciden con la entrada
        print("\n"+"=" * 54)
        print(f" Paises que coinciden con '{pais_busqueda}': ")
        print("=" * 54)
        # Recorro la lista de paises buscando coincidencias
        for pais in paises:
            pais_dataset = pais["NOMBRE"].lower()
            # Si hay coincidencia marco que se encontro y lo muestro en pantalla
            if pais_busqueda in pais_dataset:
                encontrado = True 
                print(f"Pais: {pais["NOMBRE"]} \nPoblacion: {pais["POBLACION"]} \nSuperficie: {pais["SUPERFICIE"]}km² \nContinente: {pais["CONTINENTE"]}")
                print("=" * 54)
        # Si no se encuentra devuelvo mensaje que no se encontro
        if not encontrado:
            print(f"\n ⚠️  No se encontro ningun pais que coincida con '{pais_busqueda}'.")
        return

    def FiltrarContinentes():
        paises = ObtenerPaises()
        if not paises:
            print("\n ⚠️  No hay paises disponibles dentro del dataset.\n")
            # Salimos de la función si no hay países
            return  
        print(f"\nIndique el continente que desea verificar")
        continente_busqueda = PedirContinente().lower()
        # Creo variable encontrado para detectar si se encontro alguna coincidencia
        encontrado = False 
        # Tabla con paises que coinciden con la entrada
        print("\n"+"=" * 54)
        print(f"✅ Paises dentro de '{continente_busqueda.title()}': ")
        print("=" * 54)
        # Recorro la lista de paises buscando coincidencias
        for pais in paises:
            continente_dataset = pais["CONTINENTE"].lower()
            # Si hay coincidencia marco que se encontro y lo muestro en pantalla
            if continente_busqueda in continente_dataset:
                encontrado = True 
                print(f"Pais: {pais["NOMBRE"]} \nPoblacion: {pais["POBLACION"]} \nSuperficie: {pais["SUPERFICIE"]}km² \nContinente: {pais["CONTINENTE"]}")
                print("=" * 54)
        # Si no se encuentra devuelvo mensaje que no se encontro
        if not encontrado:
            print(f"\n ⚠️  No se encontro ningun pais que este dentro de '{continente_busqueda}'.")
        return
    
    def FiltrarRangoPoblacion():
        paises = ObtenerPaises()
        if not paises:
            print("\n ⚠️  No hay paises disponibles dentro del dataset.\n")
            # Salimos de la función si no hay países
            return    
        print(f"\nIndique el MINIMO del rango de poblacion que desea verificar")
        min_rango = PedirCantidad()
        print(f"\nIndique el MAXIMO del rango de poblacion que desea verificar")
        max_rango = PedirCantidad()
        # Creo variable encontrado para detectar si se encontro alguna coincidencia
        encontrado = False 
        # Tabla con paises que coinciden con la entrada
        print("\n"+"=" * 54)
        print(f"✅ Paises dentro del rango de poblacion: '{min_rango} - {max_rango}' ")
        print("=" * 54)
        # Recorro la lista de paises buscando coincidencias
        for pais in paises:
            poblacion_dataset = pais["POBLACION"]
            # Si hay coincidencia marco que se encontro y lo muestro en pantalla
            if  min_rango <= poblacion_dataset <= max_rango:
                encontrado = True 
                print(f"Pais: {pais["NOMBRE"]} \nPoblacion: {pais["POBLACION"]} \nSuperficie: {pais["SUPERFICIE"]}km² \nContinente: {pais["CONTINENTE"]}")
                print("=" * 54)
        # Si no se encuentra devuelvo mensaje que no se encontro
        if not encontrado:
            print(f"\n ⚠️  No se encontro ningun pais que este dentro del rango de poblacion:  '{min_rango} - {max_rango}'.")
        return
        
        
        
        
        
        
        
        
    def FiltrarPaises():
        # Lista que contiene las opciones de filtro
        filtro = ["1. Filtrar por Continente",
                "2. Filtrar por Rango de poblacion",
                "3. Filtrar por Rango de superficie",
                "4. Volver al menu principal"]
        while True:
            # Mostramos las opciones del menu al usuario
            print("\n"+"="*54)
            print(" Elija una opción") 
            print("="*54)
            for opcion in filtro:
                print(opcion)
            print("="*54)
            # Pedimos al usuario que seleccione una de las opciones
            seleccion = input("Opción seleccionada: ").strip()
            print("="*54)
            match seleccion:
                case "1":
                    FiltrarContinentes()
                case "2":
                    FiltrarRangoPoblacion()
                case "3":
                    FiltrarRangoSuperficie()
                case "4":
                    print("✅ Volviendo al menu principal...\n")
                    break
                # Opcion inválida
                case _:
                    print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 4.\n")
                    continue
        return        
                
                

# Lista que contiene las opciones del menu principal
    menu_principal = ["1. Agregar pais",
                    "2. Actualizar poblacion y superficie de un pais",
                    "3. Buscar un pais",
                    "4. Filtrar paises",
                    "5. ",
                    "6. ",
                    "7. Salir"]
    while True:
        # Mostramos las opciones del menu al usuario
        print("\n"+"="*54)
        print("Bienvenido al menu de paises, elija una opción") 
        print("="*54)
        for opcion in menu_principal:
            print(opcion)
        print("="*54)
        # Pedimos al usuario que seleccione una de las opciones
        seleccion = input("Opción seleccionada: ").strip()
        print("="*54)
        match seleccion:
            case "1":
                # Agregar un país con todos los datos necesarios para almacenarse 
                # (No se permiten campos vacios)
                AgregarPais()
            case "2":
                # Actualizar los datos de Población y Superfice de un Pais
                ActualizarDatos()
            case "3":
                # Buscar un país por nombre (coincidencia parcial o exacta)
                BuscarPais()
            case "4":
                # Filtrar países por:
                #    o Continente
                #    o Rango de población
                #    o Rango de superficie
                FiltrarPaises()
            case "5":
                #  Ordenar países por:
                #    o Nombre
                #    o Población
                #    o Superficie (ascendente o descendente) 
                OrdenarPaises()
            case "6":
                # Mostrar estadísticas: 
                #    o País con mayor y menor población
                #    o Promedio de población
                #    o Promedio de superficie
                #    o Cantidad de países por continente 
                MostrarEstadisticas()
            case "7":
                print("✅ Saliendo del programa... ¡Hasta luego!\n")
                break
            # Opcion inválida
            case _:
                print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 7.\n")
                continue            
    
#=========================================================================================#
#                              Ejecuto el programa principal                              #
#=========================================================================================#
programa_principal()
#=========================================================================================#