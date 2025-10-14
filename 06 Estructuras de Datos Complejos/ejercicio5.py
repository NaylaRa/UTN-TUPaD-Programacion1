frase = input("Ingrese una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("\nPalabras_únicas:", palabras_unicas)
print("Recuento:", recuento)