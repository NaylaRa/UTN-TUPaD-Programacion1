import random
from statistics import mean, median, mode

# Generar una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

# Calcular media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostrar valores
print("Lista de números:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo (distribución normal)")
else:
    print("No se cumple un sesgo claro entre los valores")