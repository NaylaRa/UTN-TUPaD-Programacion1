contactos = {}
print("=== CARGAR CONTACTOS ===")

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el número telefónico de {nombre}: ")
    contactos[nombre] = telefono
    print(f"Contacto '{nombre}' agregado exitosamente.\n")

print("\n=== CONSULTAR CONTACTOS ===")
while True:
    nombre_buscar = input("Ingrese el nombre a consultar (o 'salir' para terminar): ")
    
    if nombre_buscar.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    if nombre_buscar in contactos:
        print(f" Número de {nombre_buscar}: {contactos[nombre_buscar]}\n")
    else:
        print(f" El contacto '{nombre_buscar}' no existe en la agenda.\n")