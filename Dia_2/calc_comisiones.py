nombre_empleado = input("Escribe tu nombre: ")
ventas_totales = float(input("Escribe el monto de tus ventas totales: "))
comision = round(ventas_totales * 0.3, 2)

print("Calculando .... \n")

print(f"Excelente {nombre_empleado}, has ganado: ${comision} MXN de comision")