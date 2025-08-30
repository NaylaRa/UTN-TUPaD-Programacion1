nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opción (1 = mayúsculas, 2 = minúsculas, 3 = primera letra mayúscula):"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida. Debe ingresar 1, 2 o 3.")