# import datetime
from datetime import datetime, date


# mi_hora = datetime.time(18, 34, 40)
# print(mi_hora)
# print(mi_hora.minute)
#
# mi_dia = datetime.date(2025, 10, 18)
# print(mi_dia)
# print(mi_dia.year)
# print(mi_dia.ctime())
# print(mi_dia.today())

mi_fecha = datetime(2024, 4, 12, 22, 10, 15)
print(mi_fecha)

mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

nacimiento = date(1995, 2, 4)
muerte = date(2093, 5, 12)

vida = muerte - nacimiento

print(vida)

despierta = datetime(2022, 10, 4, 7, 10)
duerme = datetime(2022, 10, 4, 23, 45)

vigilia = duerme - despierta
print(vigilia)
print(vigilia.seconds)


hoy = date.today()
print(hoy)

minutos = datetime.now().minute
print(minutos)
