numeros = [1, 2, 3, 4, 5, 6, 7]
rotacion_cantidad = -1

nuevos_numeros = numeros[rotacion_cantidad:] + numeros[:rotacion_cantidad]

print('Lista antes:', numeros)
print('Lista después:', nuevos_numeros)