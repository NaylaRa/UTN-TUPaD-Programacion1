def tabla_multiplicar(numero):
    print("Tabla de multiplicar del", numero)
    for i in range(1, 11):   
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

num = int(input("Ingrese un número: "))
tabla_multiplicar(num)
