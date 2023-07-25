from random import randint

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_cuenta(self):
        print(f"""Hola {self.nombre} {self.apellido}, estos son tus datos bancarios:
        Tu numero de cuenta es: {self.numero_cuenta}
        Tu balance actual es: {round(self.balance, 2)}
        """)

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Deposito realizado con Exito!")

    def retirar(self, cantidad):
        while cantidad > self.balance:
            print("Saldo Insuficiente :(")
            cantidad = float(input("Ingresa otra cantidad: "))
        else:
            self.balance -= cantidad
            print("Retiro Exitoso!")


def crear_cliente():
    print("Ingresa la siguiente informacion para crear tu cuenta: ")

    nombre = input("Ingresa solo tu nombre, sin apellidos: ")
    apellidos = input("Ingresa tus apellidos: ")

    print("A continuacion se generara tu numero de cuenta...")
    numero_cuenta = 35798345 * randint(10, 21)
    balance = 0.0

    cliente_nuevo = Cliente(nombre, apellidos, numero_cuenta, balance)

    return cliente_nuevo


def menu():

    eleccion_usuario = 'x'

    while not eleccion_usuario.isnumeric() or int(eleccion_usuario) not in range(1, 5):
        print("#" * 50)
        print("""Menu: 
        [1] -> Imprimir Cuenta
        [2] -> Depositar
        [3] -> Retirar
        [4] -> Salir
        """)
        print("#" * 50)

        eleccion_usuario = input("Selecciona la accion que desear realizar: ")

    return int(eleccion_usuario)

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresiona la 'v' para volver al menu: ")

def inicio():
    print("Hola bienvenido a BANCOMEX")
    print("A continuacion crearemos tu cuenta de banco: ")

    cliente = crear_cliente()

    print("Cuenta generada con Exito.")

    finalizar_programa = False


    while not finalizar_programa:
        eleccion = menu()

        if eleccion == 1:
            cliente.imprimir_cuenta()
            volver_inicio()
        elif eleccion == 2:
            print(f"Saldo actual: {cliente.balance}MXN")
            deposito = float(input("Ingresa la cantidad a depositar: "))
            cliente.depositar(deposito)
            volver_inicio()
        elif eleccion == 3:
            print(f"Saldo actual: {cliente.balance}MXN")
            if cliente.balance <= 0.0:
                print("Tu saldo es 0, no puedes retirar.")
                continue
            retiro = float(input("Ingresa la cantidad a retirar: "))
            cliente.retirar(retiro)
            volver_inicio()
        elif eleccion == 4:
            print(f"Hasta Pronto {cliente.nombre}...")
            finalizar_programa = True


inicio()
