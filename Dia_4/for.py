weekdays = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

for day in weekdays:
    if len(day) > 6:
        print(f"Hoy es: { day } { weekdays.index(day) + 1}")

for letra in "Alexis":
    print(letra)

data = {
    "name": "Alexis",
    "username": "alexdev2808",
    "age": 18
}

for key, value in data.items():
    print(key, value)


#rangos

print("*" * 20)

for num in range(0, 13, 2):
    print(num)

lista = list(range(1, 101))
print(lista)

