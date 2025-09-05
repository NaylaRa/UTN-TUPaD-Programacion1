cantidad = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
print(f" Ingrese {cantidad} números enteros:")
for i in range(cantidad):
    num = int(input(f"Número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("\n Resultados:")
print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)