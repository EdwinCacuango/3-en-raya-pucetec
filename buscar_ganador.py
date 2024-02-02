def buscar_filas(posiciones):
    for i in range(3):
        if posiciones[i][0] == posiciones[i][1] == posiciones[i][2]:
            return f"{posiciones[i][0]}"   

def buscar_columnas(posiciones):
    for i in range(3):
        if posiciones[0][i] == posiciones[1][i] == posiciones [2][i]:
            return f"{posiciones[0][i]}"
    return "Sigue participando"

def buscar_diagonales(posiciones):
    counter_o = 0
    counter_x = 0

    for i in range(len(posiciones)-1):
        if posiciones[i][i] == "X":
            counter_x += 1
        elif posiciones[i][i] =="O":
            counter_o +=1

    
    if counter_o == 3:
        return "O"
    elif counter_x == 3:
        return "X"
    elif posiciones[0][2] == posiciones[1][1] == posiciones [3][0]:
        return posiciones [0][2]
    else:
        return "Sigue participando"

def buscar_empate(posiciones):
    for item in posiciones:
        if item is not int:
            return "Empate - Juego finalizado"
        
def buscar_ganador(posiciones):
    if not posiciones:
        return False

    if buscar_filas(posiciones) == "X" or buscar_columnas(posiciones) == "X" or buscar_diagonales(posiciones) == "X":
        return "La PC ha ganado"
    elif buscar_filas(posiciones) == "O" or buscar_columnas(posiciones) == "O" or buscar_diagonales(posiciones) == "O":
        return "Felicidades, ha ganado"
    elif "Empate" in buscar_empate(posiciones):
        return "EMPATE - Fin del juego"
    else:
        return False


