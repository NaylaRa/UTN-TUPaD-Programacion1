datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

nuevos_datos = []
for num in datos:
    if num not in nuevos_datos:
        nuevos_datos.append(num)

print("Los datos son (orden original):", nuevos_datos)