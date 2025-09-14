notas = [[8,7,9], [6,8,7], [9,9,10], [7,6,8], [8,7,9]]
materias = ["Matemática", "Física", "Química"]

print("Promedios estudiantes:")
for i, est in enumerate(notas, 1):
    print(f"Est {i}: {sum(est)/3:.2f}")

print("\nPromedios materias:")
for j in range(3):
    prom = sum(est[j] for est in notas) / 5
    print(f"{materias[j]}: {prom:.2f}")