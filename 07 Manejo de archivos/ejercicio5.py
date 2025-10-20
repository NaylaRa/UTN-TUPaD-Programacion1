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

nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")
