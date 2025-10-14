agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

while True:
    dia = input("Ingrese el día (o 'salir' para terminar): ").lower()
    if dia == 'salir':
        break
    
    hora = input("Ingrese la hora (HH:MM): ")
    
    clave = (dia, hora)
    
    if clave in agenda:
        print(f"Evento: {agenda[clave]}")
        modificar = input("¿Modificar evento? (s/n): ").lower()
        if modificar == 's':
            nuevo_evento = input("Nuevo evento: ")
            agenda[clave] = nuevo_evento
            print("Evento actualizado")
    else:
        print("No hay evento programado")
        agregar = input("¿Agregar evento? (s/n): ").lower()
        if agregar == 's':
            evento = input("Ingrese el evento: ")
            agenda[clave] = evento
            print("Evento agregado")
    
    print()