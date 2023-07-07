nombres = ["Alex", "Fede", "Valeria", "Hugo"]
edades = [22, 39, 23, 53, 51]
ciudades = ['Mexico', 'Colombia', 'Bolivia', 'Argentina']

combinacion = list(zip(nombres, edades, ciudades))
print(combinacion)

for nombre, edad, ciudad in combinacion:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")
