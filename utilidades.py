# Funcion para buscar en posiciones un numero y devolver la fila y columna
def buscar_y_reemplazar (numero, jugada, posiciones):
    for i in range(3):
        for j in range(3):
            if posiciones[i][j] == numero:
                posiciones[i][j] = jugada


def buscar(numero, posiciones):
    for i in range(3):
        for j in range(3):
            if posiciones[i][j] == numero:
                return (i, j)


        
