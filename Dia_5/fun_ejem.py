precios_cafe = [('capuccino', 1.1), ('Expresso', 1.4), ('Moka', 1.7)]


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            mas_caro = cafe
        else:
            pass

    return (mas_caro, precio_mayor)


cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El cafe mas caro es: {cafe}, cuyo precio es: ${precio}")
