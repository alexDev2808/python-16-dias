mi_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
segunda_lista = ['z', 'x', 'y', 'w']
print(type(mi_lista))
print(len(mi_lista))

parte_lista = mi_lista[1:6] # No es inclusivo
print(parte_lista)

mi_lista[0] = 'a: alexis'

tercera_lista = mi_lista + segunda_lista
print(tercera_lista)

tercera_lista.append("Append")
print(tercera_lista)

valor_eliminado = tercera_lista.pop(0)
print(tercera_lista)
print(valor_eliminado)

# Sort

tercera_lista.sort()
print(tercera_lista)

tercera_lista.reverse()
print(tercera_lista)

