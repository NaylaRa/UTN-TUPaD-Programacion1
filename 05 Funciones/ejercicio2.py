def saludar_usuario(nombre):
    saludo = "Hola " + nombre + "!"
    return saludo

nombre_ingresado = input("Ingrese su nombre: ")
mensaje = saludar_usuario(nombre_ingresado)
print(mensaje)
