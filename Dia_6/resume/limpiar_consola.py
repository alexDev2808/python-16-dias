from os import system

def detectar_sistema_operativo():
    """Detecta el sistema operativo y devuelve el comando para limpiar la consola."""
    if system().lower() == 'windows':
        return 'cls'
    else:
        return 'clear'
    

def main():
    cmd_os = detectar_sistema_operativo()
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    system(cmd_os)  # Limpia la consola
    print(f"¡Hola, {nombre}! Tienes {edad} años.")

if __name__ == "__main__":
    main()