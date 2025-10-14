original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Uruguay": "Montevideo"}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Original:", original)
print("Invertido:", invertido)