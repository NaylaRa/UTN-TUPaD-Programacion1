ventas = [
    [10, 12, 15, 20, 18, 22, 25],  # Producto 1
    [5, 7, 8, 6, 10, 12, 9],       # Producto 2
    [20, 18, 22, 25, 24, 30, 28],  # Producto 3
    [12, 14, 10, 15, 17, 19, 16]   # Producto 4
]

print("Total vendido por producto:")
totales_productos = []
for i, fila in enumerate(ventas):
    total = sum(fila)
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")

totales_dias = [sum(ventas[fila][col] for fila in range(4)) for col in range(7)]
dia_mayor = totales_dias.index(max(totales_dias)) + 1
print(f"\nEl día con mayores ventas fue el día {dia_mayor} con {max(totales_dias)} ventas.")

producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print(f"\nEl producto más vendido en la semana fue el Producto {producto_mas_vendido} con {max(totales_productos)} ventas.")
