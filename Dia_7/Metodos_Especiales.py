mi_lista = [1,1,1,11,1,1]
print(len(mi_lista))

class Objeto:
    pass


mi_obj = Objeto()
# print(len(mi_obj))

class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # metodo especial __str__
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el CD")


mi_cd = CD('ACDC', "Back In Black", 18)

print(mi_cd)
print(len(mi_cd))


del mi_cd

# No funciona porque se elimino
# print(mi_cd)
