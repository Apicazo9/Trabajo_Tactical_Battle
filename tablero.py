# Crear un diccionario para representar el tablero
tablero = {}

# Inicializar el tablero
for fila in range(1, 5):
    for columna in ['a', 'b', 'c', 'd']:
        casilla = f"{columna}{fila}"
        tablero[casilla] = ""
        tablero[casilla] = None

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in range(1, 5):
        for columna in ['a', 'b', 'c', 'd']:
            casilla = f"{columna}{fila}"
            print(tablero[casilla], end=" | ")
        print()

# Ejemplo de uso



imprimir_tablero(tablero)
