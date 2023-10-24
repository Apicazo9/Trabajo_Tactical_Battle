import tablero

max_raw = 4
max_col = 'd'

# comprobar si una posicion es valida
def validar_celda (celda, max_col, max_raw) -> bool:
    return (celda[0] >= 'a' and celda[0] <= max_col) and (celda[1] >= '1' and celda[1] <= str(max_raw))


# comprobar si un miembro del equipo ya ocupa una celda dada
def comprobar_celda_disponible(celda, equipo) -> bool:
     return tablero.tablero[celda] == equipo   #me falta ver como has hecho las listas de los equipos ;)


# comprobar celda contigua
def validar_celda_contigua(celda1, celda2):
    return (chr(ord(celda1[0]) + 1) == celda2[0] or chr(ord(celda1[0]) - 1) == celda2[0]) or (chr(ord(celda1[1]) + 1) == celda2[1] or chr(ord(celda1[1]) - 1) == celda2[1])

# mover celda
def mover_celda_contigua(celda1, celda2):
    if (validar_celda(celda1, max_col, max_raw) and validar_celda(celda2, max_col, max_raw)) and (validar_celda_contigua(celda1, celda2)):
        tablero.tablero[celda2] = tablero.tablero[celda1]
        tablero.tablero[celda1] = None
