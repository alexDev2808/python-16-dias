"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valor intermedio.
"""

def devolver_distintos(num1, num2, num3):
    sum = num1 + num2 + num3
    lista_num = [num1, num2, num3]

    print(f"La suma total es: {sum}")

    if sum > 15:
        return max(lista_num)
    if sum < 10:
        return min(lista_num)
    else:
        lista_num.sort()
        return lista_num[1]


print(devolver_distintos(18, 8, 5))

# Versión más corta:

def devolver_distintos(num1: int, num2: int, num3: int) -> int:
    nums = [num1, num2, num3]
    if sum(nums) > 15:
        return max(nums)
    if sum(nums) < 10:
        return min(nums)
    return sorted(nums)[1]


print(devolver_distintos(18, 8.9, 5))