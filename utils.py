import tablero

max_row = 4
max_col = 'd'

# comprobar si una posicion es valida
def validar_celda (celda, max_col, max_row) -> bool:
    return (celda[0] >= 'a' and celda[0] <= max_col) and (celda[1] >= '1' and celda[1] <= str(max_row))


# comprobar si un miembro del equipo ya ocupa una celda dada
def comprobar_celda_disponible(celda, equipo) -> bool:
     return tablero.tablero[celda] == equipo   #me falta ver como has hecho las listas de los equipos ;)


# comprobar celda contigua
def validar_celda_contigua(celda_actual, celda_nueva):
    return (chr(ord(celda_actual[0]) + 1) == celda_nueva[0] or chr(ord(celda_actual[0]) - 1) == celda_nueva[0]) or (chr(ord(celda_actual[1]) + 1) == celda_nueva[1] or chr(ord(celda_actual[1]) - 1) == celda_nueva[1])

# mover celda
# le he cambiado el nombre de mover_celda_contigua a mover
def mover(celda_nueva, celda_actual):
    col = celda_nueva[0]
    row = celda_nueva[1]
    if validar_celda(celda_nueva, max_col, max_row) and validar_celda_contigua(col, row):
        self.posicion

        #tablero.tablero[row] = tablero.tablero[row]
        #tablero.tablero[row] = None
