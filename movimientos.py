from utilidades import buscar_y_reemplazar, buscar
import random

def nueva_jugada_usuario(posiciones):
    eleccion_correcta = False

    while not eleccion_correcta:
        eleccion_usuario = input("Ingresa la posición disponible: ")

        # Validación de que el input sea un dígito
        if not eleccion_usuario.isdigit():
            print("Error: Debes ingresar un número, no una letra")
            continue

        eleccion_usuario = int(eleccion_usuario)

        # Validación de que el número ingresado este disponible y sea correcto
        if buscar(eleccion_usuario, posiciones) == None:
            print("Posición ocupada.")
            print("Intente de nuevo. No olvides que las posiciones válidas son del 1 al 9 y deben mostrarse en el tablero")
        else:
            # Si el numero es correcto, se busca nuevamente y se reemplaza con O
            buscar_y_reemplazar(eleccion_usuario, "O", posiciones)
            eleccion_correcta = True

def nueva_jugada_maquina(posiciones):
    random_value = random.randint(1, 10)

    # Buscar valores disponibles
    while buscar(random_value, posiciones) is None:
        random_value= random.randint(1,10)
    
    # Crear la jugada en la posicion disponible
    buscar_y_reemplazar(random_value, "X", posiciones)
