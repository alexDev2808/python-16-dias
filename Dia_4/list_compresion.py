palabra = "Alexis"

lista = [letra for letra in palabra]
lista2 = [num for num in range(0, 21, 2)]
lista3 = [num / 2 for num in range(1, 41)]
lista4 = [num / 3 if num * 2 > 10 else "No" for num in range(0, 59, 3)]

pies = [10, 30,50 ,60, 35, 60]
metros = [round(num * 0.3048, 3) for num in pies]

print(lista)
print(lista2)
print(lista3)
print(lista4)
print(metros)
