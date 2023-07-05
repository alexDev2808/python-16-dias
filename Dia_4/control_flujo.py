
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes votar")
elif edad >= 15 and edad < 18:
    print("Puedes solicitar tu pre-credencial")
else:
    print("No puedes votar")