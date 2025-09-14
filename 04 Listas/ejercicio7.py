temperaturas = [
    [4, 16],
    [3, 16],
    [5, 14],
    [6, 15],
    [4, 20],  
    [10, 20],
    [15, 22]
]

promedios = [None, None]  # [min, max]
mayor_amplitud = [None, None]  # [dia, amplitud]
temps_min = []
temps_max = []

for dia, temp_dia in enumerate(temperaturas):
    temps_min.append(temp_dia[0])
    temps_max.append(temp_dia[1])
    amplitud_term = temp_dia[1] - temp_dia[0]
    
    if mayor_amplitud[1] is None or mayor_amplitud[1] < amplitud_term:
        mayor_amplitud = [dia, amplitud_term]

promedios[0] = sum(temps_min) / len(temps_min)
promedios[1] = sum(temps_max) / len(temps_max)

print('Promedio minimo:', promedios[0])
print('Promedio maximo:', promedios[1])
print(f'Mayor amplitud termica registrada: Dia {mayor_amplitud[0]} (con {mayor_amplitud[1]}°)')