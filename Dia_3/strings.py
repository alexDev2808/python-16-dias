texto = "Mi nombre es J. Alexis TH"
resultado = texto[len(texto) - 1]
index = texto.index("T") # se detiene a la primera coincidencia
index_desde = texto.index("e", 9, 18)
index_reversa = texto.rindex("e")


print(resultado)
print(index)
print(index_desde)
print(index_reversa)


#Extraer substrings

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fragmento = abecedario[2:5] # el final no es inclusivo
print(fragmento)

fragmento2 = abecedario[4:]
print(fragmento2)

fragmento3 = abecedario[2:20:2]
print(fragmento3)

fragmento4 = abecedario[::-1]
print(fragmento4)


#Metodos de strings

texto_ejemplo = "Trabajando con los metodos de los strings en Python."

texto_upper = texto_ejemplo[3:15].upper()
print(texto_upper)

texto_split = texto_ejemplo.split() # Por defecto los separa por los espacios
print(texto_split)

lenguaje = "Python"
version = "3.10"
meta = "Aprender Desarrollo Web con"

union = " ".join([meta, lenguaje, version])
print(union)

texto_escondido = "Encuentra la palabra que quieras d3ntr0 de este texto"
encontrar = texto_escondido.find("0")
print(encontrar)

texto_a_remplazar = "Puedes remplazar cualquier parte de este texto de ejemplo"
texto_a_remplazar_resultado = texto_a_remplazar.replace("e", "i")
print(texto_a_remplazar_resultado)


#Propiedades de los strings

nombre = "Tania"
# nombre[0] = "D" esto no es posible porque los strings son inmutables

print(nombre * 10)

texto_multilinea = """
    Este es un texto
    con varias lineas,
    esto es posible con 3 comillas dobles
    al inicio y al final
"""

print(texto_multilinea)

print("posible" in texto_multilinea)
print("posible" not in texto_multilinea)
print(len(nombre))
