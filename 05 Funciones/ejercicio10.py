def calcular_promedio(a, b, c):
    """Calcula el promedio de tres números."""
    promedio = (a + b + c) / 3
    return promedio

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {resultado:.2f}")
