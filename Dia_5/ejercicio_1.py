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


print(devolver_distintos(8, 1, 2))
