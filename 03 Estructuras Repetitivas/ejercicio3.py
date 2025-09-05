inicio = int(input("Ingrese el primer valor: "))
fin = int(input("Ingrese el segundo valor: "))
suma = 0 
for i in range(inicio + 1, fin):
    suma += i
print("La suma de los números entre: ", inicio, "y", fin, "es: ", suma)
