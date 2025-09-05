total = 0
while True:
    num = int(input("Ingrese un número entero (0 para terminar): "))
    if num == 0:
        break
    total += num
print("La suma total de los números ingresados es:", total)