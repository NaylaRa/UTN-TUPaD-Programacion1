import random

numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista de números generados:", numeros)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("\nNúmeros pares:", pares)
print("Números impares:", impares)

print("\nCantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))
