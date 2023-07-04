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