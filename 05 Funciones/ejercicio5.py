def segundos_a_horas(segundos):
    horas = segundos / 3600   
    return horas

segundos_ingresados = float(input("Ingrese la cantidad de segundos: "))

resultado = segundos_a_horas(segundos_ingresados)

print("Equivale a", resultado, "horas.")
