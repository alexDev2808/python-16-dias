"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla
todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""

def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2


    print(primos)
    return len(primos)


print(contar_primos(7))

# Versión 2:
def mostrar_primos(numero: int) -> int:
    total_primos = 0
    for num in range(2, numero + 1):
        divisores = 0
        for n in range(1,num + 1):
            if num % n == 0:
                divisores += 1
        if divisores == 2:
            print(num)
            total_primos += 1
    return total_primos
    
print(f"Total de números primos encontrados: {mostrar_primos(13)}")