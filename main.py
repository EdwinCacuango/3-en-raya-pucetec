from posiciones_iniciales import init
from movimientos import nueva_jugada_usuario, nueva_jugada_maquina
from buscar_ganador import buscar_ganador
from tablero import imprimir_tablero

posiciones = init()

print("\n Empecemos. Turno de la PC")
imprimir_tablero(posiciones)

print("\nTurno del jugador")
nueva_jugada_usuario(posiciones)

answer = buscar_ganador(posiciones)

while answer is False:
    nueva_jugada_maquina(posiciones)
    answer = buscar_ganador(posiciones)
    print("\n")

    if answer is False:
        imprimir_tablero(posiciones)

        nueva_jugada_usuario(posiciones)
        answer = buscar_ganador(posiciones)

    if answer is not False and "ha ganado" in answer:
        print(answer)
        imprimir_tablero(posiciones)
        break










