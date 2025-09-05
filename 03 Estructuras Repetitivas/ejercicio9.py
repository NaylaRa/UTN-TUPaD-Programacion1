cantidad = 100
suma = 0 
print(f" Ingrese {cantidad} números enteros:")
for i in range(cantidad):
    num = int(input(f"Número {i+1}: "))
    suma += num
    media = suma / cantidad
print("\n Resultados:")
print("La suma total es:", suma)
print("La media de los números ingresados es:", media)