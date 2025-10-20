with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        precio = float(datos[1])
        cantidad = int(datos[2])
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
