productos = {"manzana": 50, "banana": 30, "naranja": 40}

while True:
    producto = input("Ingrese el producto (o 'salir' para terminar): ").lower()
    
    if producto == 'salir':
        break
    
    if producto in productos:
        print(f"Stock de {producto}: {productos[producto]}")
        agregar = input("¿Agregar unidades? (s/n): ").lower()
        if agregar == 's':
            unidades = int(input("¿Cuántas unidades queres agregar?: "))
            productos[producto] += unidades
            print(f"Nuevo stock de {producto}: {productos[producto]}")
    else:
        print(f"Producto '{producto}' no existe")
        agregar = input("¿Agregar nuevo producto? (s/n): ").lower()
        if agregar == 's':
            stock = int(input("Ingrese stock inicial: "))
            productos[producto] = stock
            print(f"Producto '{producto}' agregado con stock {stock}")