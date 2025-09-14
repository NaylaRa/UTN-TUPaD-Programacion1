notas = []

for i in range(10):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    notas.append(nota)

print("\nNotas de los estudiantes:", notas)

promedio = sum(notas) / len(notas)
print("Promedio de las notas:", promedio)

nota_max = max(notas)
nota_min = min(notas)

print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)