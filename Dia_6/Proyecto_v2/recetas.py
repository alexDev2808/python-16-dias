import os
from pathlib import Path
from os import system
from shutil import rmtree

mi_ruta = Path(Path.home(), "Recetas")


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador


def inicio():
    system("clear")
    print("🗃️" * 26)
    print("\t\t" + "*" * 5 + " Bienvenido a tu Gestor de Recetas " + "*" * 5)
    print(f"\t\tLa ruta de acceso a tus recetas es: {mi_ruta}")
    print(f"\t\tActualmente hay {contar_recetas(mi_ruta)} recetas")
    print("🗃️" * 26)

    eleccion_menu = 'x'

    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("#" * 60)
        print("""MENU:
        [1] -> Leer receta
        [2] -> Crear receta
        [3] -> Crear categoria
        [4] -> Eliminar receta
        [5] -> Eliminar categoria
        [6] -> Finalizar programa
        """)
        print("#" * 60)

        eleccion_menu = input("Elige una opcion: ")

    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] -> {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")

    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] -> {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas


def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")

    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False

    while not existe:
        nombre_receta = input("Escribe el nombre de tu receta: ") + ".txt"
        contenido_receta = input("Escribe el contenido de tu receta: ")

        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Receta: {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")


def crea_categoria(ruta):
    existe = False

    while not existe:
        nombre_categoria = input("Escribe el nombre de la nueva categoria: ")

        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Categoria: {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta: {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    # Path(categoria).rmdir()
    ruta_categoria = Path(categoria)
    rmtree(ruta_categoria)
    print(f"La categoria: {categoria.name} ha sido eliminada")


def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresiona la 'v' para volver al menu: ")


finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas en esta categoria.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crea_categoria(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas en esta categoria.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True
