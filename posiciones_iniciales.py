from utilidades import buscar_y_reemplazar

def init ():
    posiciones = []  # Inicialización de la matriz vacía
    contador = 1  # Inicialización del contador

    for i in range(3):  
        fila = []  # Inicialización de la fila actual
        for j in range(3):  # Bucle interno para las columnas
            fila.append(contador)  # Agregar el número actual a la fila
            contador += 1  # Incrementar el contador
        posiciones.append(fila)  # Agregar la fila completa a la matriz
        
    #La primera jugada de la máquina es la X en el centro del tablero
    buscar_y_reemplazar(5, "X", posiciones) 

    return posiciones


