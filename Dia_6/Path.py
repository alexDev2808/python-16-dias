from pathlib import Path

# base = Path.home()
# guia = Path(base, "Barcelona", "ejem.txt")
#
# guia2 = guia.with_name("Tlaxcala.txt")
#
# print(base)
# print(guia)
# print(guia2)
#
# print(guia.parent.parent)

guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)

tour = Path("Europa", "Berlin", "Portugal", "Barcelona", "CampNou.txt")
en_europa = tour.relative_to(Path("Europa"))
en_Portugal = tour.relative_to(Path("Europa", "Berlin"))

print(en_europa)
print(en_Portugal)




