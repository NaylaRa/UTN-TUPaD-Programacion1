contraseña = input("Ingrese la contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")