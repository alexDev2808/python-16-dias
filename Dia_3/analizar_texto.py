
python = {
    "True": "SI",
    "False": "NO"
}

texto_ingresado = input("Ingresa un texto: ").lower()

letra_1 = input("Ingresa la primer letra: ").lower()
letra_2 = input("Ingresa la segunda letra: ").lower()
letra_3 = input("Ingresa la tercera letra: ").lower()

# Alternativa para contar la cantidad de aparaciones
# apariciones_letra_1 = len(texto_ingresado.split(letra_1)) - 1
# apariciones_letra_2 = len(texto_ingresado.split(letra_2)) - 1
# apariciones_letra_3 = len(texto_ingresado.split(letra_3)) - 1

apariciones_letra_1 = texto_ingresado.count(letra_1)
apariciones_letra_2 = texto_ingresado.count(letra_2)
apariciones_letra_3 = texto_ingresado.count(letra_3)


frase_invertida = texto_ingresado.split()
frase_invertida.reverse()

python_aparece = str("python" in texto_ingresado)

print(f"""
La letra: {letra_1} aparece {apariciones_letra_1}
La letra: {letra_2} aparece {apariciones_letra_2}
La letra: {letra_3} aparece {apariciones_letra_3}

Hay {len(texto_ingresado.split())} palabras en total

La primera letra es: '{texto_ingresado[0]}' y la ultima letra es: '{texto_ingresado[-1]}'

Frase en orden inverso: {" ".join(frase_invertida)}

La palabra 'python' {python[python_aparece]} aparece en el texto ingresado.
""")

