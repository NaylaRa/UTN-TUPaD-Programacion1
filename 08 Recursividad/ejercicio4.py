def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número entero positivo: "))

if num == 0:
    print("El número en binario es: 0")
else:
    print("El número en binario es:", decimal_a_binario(num))
