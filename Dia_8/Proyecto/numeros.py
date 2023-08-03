def turnos_perfumeria():
    inicio = 1

    while True:
        yield inicio
        inicio += 1


def turnos_farmacia():
    inicio = 1

    while True:
        yield inicio
        inicio += 1


def turnos_cosmeticos():
    inicio = 1

    while True:
        yield inicio
        inicio += 1


perfumeria = turnos_perfumeria()
farmacia = turnos_farmacia()
cosmeticos = turnos_cosmeticos()


def imprimir_ticket(area):
    if area == '1':
        print(f"P-0{next(perfumeria)}")
    elif area == '2':
        print(f"F-0{next(farmacia)}")
    elif area == '3':
        print(f"C-0{next(cosmeticos)}")


def decorar_saludo(funcion):
    def imprimir_turno(area):
        print("#" * 50)
        print('\nSu turno es:')
        funcion(area)
        print('Aguarde y sera atendido.\n')
        print("#" * 50)

    return imprimir_turno
