productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        productos.append(producto)

nombre_buscar = input("Ingrese el nombre del producto a actualizar: ")

for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        p["precio"] = float(input("Nuevo precio: "))
        p["cantidad"] = int(input("Nueva cantidad: "))
        print("Producto actualizado.")
        break
else:
    print("Producto no encontrado.")

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo actualizado correctamente.")
