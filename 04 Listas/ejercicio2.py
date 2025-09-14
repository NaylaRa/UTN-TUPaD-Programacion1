productos = []

for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)

productos_ordenados = sorted(productos)
print("\nLista de productos ordenados alfabéticamente:")
print(productos_ordenados)

eliminar = input("\nIngrese el producto que desea eliminar: ")

if eliminar in productos_ordenados:
    productos_ordenados.remove(eliminar)
    print("\nProducto eliminado correctamente.")
else:
    print("\nEl producto no se encontró en la lista.")


print("Lista actualizada de productos:")
print(productos_ordenados)
