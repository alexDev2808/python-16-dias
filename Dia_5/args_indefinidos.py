def suma(*args):
    return sum(args)


print(suma(45, 20))
print(suma(45, 20, 64, 23))
print(suma(45, 20, 43))


def multiplicacion(**kwargs):
    total = 1

    for clave, valor in kwargs.items():
        print(f"{clave} => {valor}")
        total *= valor

    return total


print \
    (multiplicacion(x=4, y=5, z=4))


def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es: {num1}")
    print(f"El segundo valor es: {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} => {valor}")


args = [23, 53, 346, 34, 534, 23]
kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}

prueba(23, 53, *args, **kwargs) # desempacar(desestructuracion) *args, **kwargs
