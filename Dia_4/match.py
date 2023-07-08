
serie = 'a'

match serie:
    case "a":
        print("Alexis")
    case "b":
        print("Belinda")
    case _:
        print("No hay coincidencias")


clientes = {'nombre': "Alexis", "edad": 22, "ocupacion": 'programador'}
pelicula = {'titulo': 'Matrix', "ficha_tecnica": {
    "protagonista": "Keanu Reaves", "lanzamiento": 2022
}}

elementos = [clientes, pelicula, "Libro"]

for elem in elementos:
    match elem:
        case {"nombre": nombre,
              'edad': edad,
              'ocupacion': ocupacion }:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo, "ficha_tecnica": {
            "protagonista": protagonista,
            "lanzamiento": lanzamiento
        }}:
            print("Es una pelicula")
            print(titulo, protagonista, lanzamiento)
        case _:
            print("No hay coincidencias :(")
