tablero = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

print('Tablero inicial:')
for fila in tablero:
    print(" ".join(fila))

jugador_turno = 1  # 1 = X, 2 = O
cantidad_jugadas = 0
hay_ganador = False

while True:
    fila = int(input("Ingrese la fila (0, 1, 2): "))
    columna = int(input("Ingrese la columna (0, 1, 2): "))

    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print('Posición inválida. Ingrese nuevamente.')
        continue
    if tablero[fila][columna] != '-':
        print('Posición ocupada. Ingrese nuevamente.')
        continue

    ficha = 'X' if jugador_turno == 1 else 'O'
    tablero[fila][columna] = ficha
    cantidad_jugadas += 1

    print('Tablero actualizado:')
    for fila_tablero in tablero:
        print(" ".join(fila_tablero))

    for i in range(3):
        if tablero[i][0] == ficha and tablero[i][1] == ficha and tablero[i][2] == ficha:
            print('El jugador', jugador_turno, 'ha ganado')
            hay_ganador = True
            break
        if tablero[0][i] == ficha and tablero[1][i] == ficha and tablero[2][i] == ficha:
            print('El jugador', jugador_turno, 'ha ganado')
            hay_ganador = True
            break
    
    if not hay_ganador:
        if tablero[0][0] == ficha and tablero[1][1] == ficha and tablero[2][2] == ficha:
            print('El jugador', jugador_turno, 'ha ganado')
            hay_ganador = True
        elif tablero[0][2] == ficha and tablero[1][1] == ficha and tablero[2][0] == ficha:
            print('El jugador', jugador_turno, 'ha ganado')
            hay_ganador = True

    if hay_ganador:
        break

    if cantidad_jugadas == 9:
        print('Empate')
        break

    jugador_turno = 2 if jugador_turno == 1 else 1
    print('\nTurno del jugador', jugador_turno)

print('Fin del juego')
