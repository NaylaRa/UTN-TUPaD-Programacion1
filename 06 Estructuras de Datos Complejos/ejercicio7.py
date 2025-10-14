parcial1 = {"Ana", "Luis", "Maria", "Carlos", "Sofia"}
parcial2 = {"Maria", "Juan", "Pedro", "Ana", "Lucia"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo un parcial:", solo_uno)

total = parcial1 | parcial2
print("Aprobaron al menos un parcial:", total)