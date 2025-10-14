alumnos = {
    "Sofia": (10, 9, 8),
    "Luis": (6, 7, 7)
}

print("=== PROMEDIOS ===")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {notas} -> Promedio: {promedio:.2f}")