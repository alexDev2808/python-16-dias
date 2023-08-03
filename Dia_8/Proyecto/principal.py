from numeros import imprimir_ticket, decorar_saludo


turno_generado = decorar_saludo(imprimir_ticket)


def menu():
    print("""
    Menu:
    1) Perfumeria
    2) Farmacia
    3) Cosmeticos
    4) Salir
    """)
    eleccion = input("Selecciona el area deseada: ")

    while not eleccion.isnumeric() or int(eleccion) not in range(1, 5):
        print("Eleccion incorrecta, vuelve a intentarlo")
        eleccion = input("Selecciona el area deseada: ")

    return eleccion


def inicio():
    print("Bienvenido a la Consola de Turnos: ")

    finalizar_programa = False

    while not finalizar_programa:
        eleccion = menu()
        if eleccion != '4':
            turno_generado(eleccion)
        else:
            print("Adios...")
            finalizar_programa = True


inicio()
