import re

# texto = "Llama al 435-533-2425 o al 246-142-4234 para solicitar mas informacion al respecto"
#
# # patron = r'\d{3}-\d{3}-\d{4}'
# patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
#
# r_todos = re.findall(patron, texto)
# res = re.search(patron, texto)
#
# print(r_todos)
# print(res)
# print(res.group(2))

# clave = input("Clave: ")
#
# formato = r'\D{1}\w{7}'
#
# comprobar = re.search(formato, clave)
#
# print(comprobar)

texto = "No atendemos los lunes por la tarde"
# buscar = re.search(r'lunes|martes', texto)
# buscar = re.search(r'...demos', texto)
# buscar = re.search(r'^\D', texto)
# buscar = re.search(r'\D$', texto)
buscar = re.findall(r'[^\s]+', texto)


print("_".join(buscar))


def verificar_email(email):
    # if re.search(r'\w+@\w+\.com$|\.com\...$', email):
    if re.search(r'@\w+\.com', email):

        return "Ok"
    else:
        return "La dirección de email es incorrecta"


print(verificar_email("usuario@host.com"))


def verificar_saludo(frase):
    if re.search("^Hola", frase):
        print("Ok")
    else:
        print("No has saludado")


verificar_saludo("Hola me llamo alexis")


def verificar_cp(cp):
    if re.search(r'\w{2}\d{4}', cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp("M90850")
