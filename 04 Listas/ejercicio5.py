estudiantes = ["León", "Antonella", "Ivan", "Juan", "Carlos", "Gonzalo", "Sofia", "Maria"]

print("Lista inicial de los estudiantes:", estudiantes)

operacion = input("\n¿Queres agregar o eliminar un estudiante? (agregar/eliminar): ").lower()

if operacion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\nEstudiante {nuevo} agregado correctamente.")

elif operacion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"\nEstudiante {eliminar} eliminado correctamente.")
    else:
        print("\nNo existe ese estudiante.")

else:
    print("\nOperacion invalida. No se hicieron cambios.")

# Mostrar lista final
print("\nLista final de estudiantes:", estudiantes)
