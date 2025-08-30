num1 = int(input("Ingresá un número entero distinto de 0: "))
while num1 == 0:
    print("El número no puede ser 0, intentá de nuevo.")
    num1 = int(input("Ingresá un número entero distinto de 0: "))

num2 = int(input("Ingresá otro número entero distinto de 0: "))
while num2 == 0:
    print("El número no puede ser 0, intentá de nuevo.")
    num2 = int(input("Ingresá otro número entero distinto de 0: "))

print(f"Suma: {num1} + {num2} = {num1 + num2}")
print(f"Resta: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")
print(f"División: {num1} / {num2} = {num1 / num2}")