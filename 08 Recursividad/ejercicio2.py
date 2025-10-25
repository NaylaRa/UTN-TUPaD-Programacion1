def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

for i in range(pos):
    print(fibonacci(i), end=" ")
