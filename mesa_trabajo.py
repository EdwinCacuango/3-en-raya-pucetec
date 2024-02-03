#Mesa de trabajo
from posiciones_iniciales import init
from movimientos import nueva_jugada_usuario, nueva_jugada_maquina
from utilidades import  buscar, buscar_y_reemplazar
from buscar_ganador import buscar_ganador, buscar_filas, buscar_columnas
from tablero import imprimir_tablero




posiciones = init()


posiciones = [
    ["X", "O", "X"],
    ["O","X", "O"],
    ["O", "X", "O"]
]






ganador = buscar_ganador(posiciones)
print(ganador)
