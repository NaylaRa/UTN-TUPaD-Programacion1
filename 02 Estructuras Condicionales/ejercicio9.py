magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"
print("La magnitud ingresada corresponde a un terremoto:", categoria)