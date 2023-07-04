mi_edad = input("Escribe tu edad: ") # input devuelve un tipo de dato string
estatura = float(input("Escribe tu estatura: ")) #casting: conversion de un tipo a otro de manera explicita
promedio = estatura * 3

print(type(promedio))
print(f"Tu altura es de {estatura}m y el promedio es: {round(promedio, 3)}") #formatear cadenas

num1 = 45
num2 = 2

print(f"El resultado es: {num1 / num2}")
print(f"El resultado es: {num1 // num2}")

print(f"Exponenciacion: {num1 ** num2}")
print(f"Raiz : {round(num1 ** 0.5, 2)}")

redondeo = 4.5

print(round(redondeo))