import math 

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio_usuario = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)
