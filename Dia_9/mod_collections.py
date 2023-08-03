from collections import Counter, defaultdict, namedtuple

numeros = [8, 59,2, 4, 2, 5,2, 12, 5,8, 9, 2, 4, 2, 1,5,6, 2]
frase = "al pan pan y al vino vino"
print(Counter(numeros))
print(Counter("misissippi"))
print(Counter(frase.split()))

serie = Counter([1,1,11,1, 3,3,3,3,33,33,333, 222,2,222,2,2])

print(serie.most_common())
print(serie.most_common(2))

print(list(serie))

mi_dict = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_dict['dos'])

mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)
print(mi_dic['tres'])
print(mi_dic)

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

mi_tupla = (500, 18, 65)
print(mi_tupla[1])

print(ariel.altura)



