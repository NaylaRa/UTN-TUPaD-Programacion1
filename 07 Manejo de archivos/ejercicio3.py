with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        precio = float(datos[1])
        cantidad = int(datos[2])
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

nombre = input("Ingrese el nombre del nuevo producto: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("Producto agregado correctamente.")
