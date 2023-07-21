class Pajaro:
    # Atributos de clase
    alas = True

    # metodo constructor (self: obligatorio -> instancia del objeto
    # __init__ se inicializa el objeto, instancias de cada objeto
    def __init__(self, nombre, color, especie):
        # Atributos de Instancia
        self.nombre_pajaro = nombre
        self.color_pajaro = color
        self.especie = especie

    def piar(self):
        print("Me llamo {}".format(self.nombre_pajaro))
        print(f"Soy de la especie de {self.especie}")
        print("Pio " * 5)

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


mi_pajaro = Pajaro("Twitter", 'azul', "Colibri")
otro_pajaro = Pajaro("Alex", 'verde', "Tucan")

print(mi_pajaro.nombre_pajaro)
print(otro_pajaro.color_pajaro)
print(Pajaro.alas)
print(otro_pajaro.alas)
print(mi_pajaro.piar())
print(mi_pajaro.volar(50))
