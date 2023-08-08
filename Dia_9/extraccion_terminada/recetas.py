import os
from os import system
from pathlib import Path
from shutil import rmtree

carpeta = Path("Proyecto", "Recetas")
ruta = carpeta.relative_to(Path("Proyecto"))


def bienvenida():
    tecla = "a"
    num_recetas = 0

    for txt in Path(ruta).glob("**/*.txt"):
        num_recetas += 1

    while tecla != 'c':
        print("🗃️" * 22)
        print("\t\tBienvenido a tu GESTOR DE RECETAS\n")
        print(f"\t\tLa ruta de acceso a tus recetas es: /{ruta}")
        print(f"\t\tActualmente hay {num_recetas} recetas")
        print("🗃️" * 22)
        tecla = input("Presiona la letra 'c' para continuar...")

    menu()


def menu():
    system('clear')
    print("#" * 60)
    print("""MENU.
    
    [1] -> Leer receta
    [2] -> Crear receta
    [3] -> Crear categoria
    [4] -> Eliminar receta
    [5] -> Eliminar categoria
    [6] -> Finalizar programa
    """)
    print("#" * 60)

    seleccion = input("Selecciona una opcion: ")

    match seleccion:
        case '1':
            leer_receta()
        case '2':
            crear_receta()
        case '3':
            crear_categoria()
        case '4':
            eliminar_receta()
        case '5':
            eliminar_categoria()
        case '6':
            print("Finalizando programa...")
            print("Adios.!")
            return 0
        case _:
            print("Opcion No Valida. Vuelve a intentarlo")
            menu()


def obtener_categorias():
    carpetas = []
    categorias = []

    for carp in Path(ruta).glob("**/"):
        carpetas.append(str(carp))

    long_carpeta = len(carpetas[0]) + 1

    for carp in carpetas:
        categoria = carp[long_carpeta:]
        if categoria == '':
            continue
        categorias.append(categoria)

    return categorias


def obtener_recetas(carpeta_elegida):
    recetas = []

    for receta in Path(ruta, carpeta_elegida).glob("*.txt"):
        recetas.append(os.path.basename(receta))

    return recetas


def obtener_recetas_categoria(seleccion):
    print(f"Seleccionaste {seleccion}")
    print("Lista de recetas disponibles: ")
    recetas = obtener_recetas(seleccion)
    for num, receta in enumerate(recetas):
        print(f"[{num + 1}] -> {receta}")

    receta_elegida = int(input("\nSelecciona el numero de la que deseas leer: "))

    return recetas[receta_elegida - 1]


def obtener_mostrar_informacion():
    categorias = obtener_categorias()

    print("Por favor Selecciona una categoria: ")

    for num, categ in enumerate(categorias):
        print(f"[{num + 1}] -> {categ}")

    seleccion = int(input("Escribe el numero de categoria: "))
    categoria_seleccionada = categorias[seleccion - 1]

    return categoria_seleccionada


def leer_receta():
    print("Opcion: LEER RECETA")

    categoria_seleccionada = obtener_mostrar_informacion()

    receta_elegida = obtener_recetas_categoria(categoria_seleccionada)

    ruta_receta = Path(ruta, categoria_seleccionada, receta_elegida)
    print(f"Seleccionaste: {receta_elegida}")

    archivo_receta = open(ruta_receta)
    contenido_receta = archivo_receta.read()
    continuar = 'n'
    while continuar != 'c':
        print("🔸" * 40)
        print(contenido_receta)
        print("🔸" * 40)
        continuar = input("Presiona la 'c' para continuar...")

    archivo_receta.close()
    menu()


def crear_receta():
    print("Opcion: CREAR RECETA")

    categoria_seleccionada = obtener_mostrar_informacion()

    ruta_crear_receta = Path(ruta, categoria_seleccionada)

    print(f"Cambiando a {ruta_crear_receta}")
    nombre_receta = input("Escribe el nombre de la receta: ")
    contenido_receta = input("Ahora escribe el contenido de la receta: ")

    os.chdir(ruta_crear_receta)

    mi_archivo = open(nombre_receta + ".txt", "w")
    mi_archivo.write(contenido_receta)
    mi_archivo.close()

    os.chdir('../../')
    print("Receta creada exitosamente!!")

    input("Presiona Enter para continuar...")
    menu()


def crear_categoria():
    print("Opcion: CREAR CATEGORIA")

    nombre = input("Escribe el nombre de la nueva categoria: ")
    ruta_crear = Path(ruta, nombre)
    print(ruta_crear)
    os.makedirs(ruta_crear)
    print("Categoria creada exitosamente!!")
    input("Presiona Enter para continuar...")
    menu()


def eliminar_receta():
    print("Opcion: ELIMINAR RECETA")

    categoria_seleccionada = obtener_mostrar_informacion()

    receta_elegida = obtener_recetas_categoria(categoria_seleccionada)

    ruta_receta = Path(ruta, categoria_seleccionada, receta_elegida)
    print(f"Seleccionaste: {receta_elegida}. Eliminando...")

    os.remove(ruta_receta)

    print("Receta eliminado con exito!.")
    input("Presiona una tecla para continuar...")
    menu()


def eliminar_categoria():
    print("Opcion: ELIMINAR CATEGORIA")

    categoria_seleccionada = obtener_mostrar_informacion()

    ruta_eliminar = Path(ruta, categoria_seleccionada)

    print(ruta_eliminar)
    rmtree(ruta_eliminar)
    print("Categoria eliminada exitosamente!!")
    input("Presiona Enter para continuar...")
    menu()


bienvenida()
