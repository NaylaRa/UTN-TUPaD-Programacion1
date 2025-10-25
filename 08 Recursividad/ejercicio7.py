def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
print("El total de bloques necesarios es:", contar_bloques(niveles))
