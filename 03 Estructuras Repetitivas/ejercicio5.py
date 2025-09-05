import random 
secreto = random.randint(0, 9)
intentos = 0 
adivinado = False
print("Adivina el número entre 0 y 9")
while not adivinado:
    num = int(input("Ingresa tu número: "))
    intentos += 1 
    if num == secreto:
        adivinado = True 
        print("¡Correcto! El número era", secreto)
        print("Lo lograste en", intentos, "intentos.") 
    else:
        print("Incorrecto, intenta de nuevo.")
