import tablero
def limpiar_terminal():
print(chr(27) + "[2J")
# comprobar si una posicion es valida
def validar_celda (celda, max_col, max_raw) -> bool:
    return (celda[0] >= 'a' and celda[0] <= max_col) and (celda[1] >= '1' and celda[1] <= str(max_raw))


# comprobar si un miembro del equipo ya ocupa una celda dada
def comprobar_celda_disponible(celda, equipo) -> bool:
     return tablero.tablero[celda] == equipo


# comprobar celda contigua
def validar_celda_contigua(celda1, celda2):
    return (chr(ord(celda1[0]) + 1) == celda2[0] or chr(ord(celda1[0]) - 1) == celda2[0]) or (chr(ord(celda1[1]) + 1) == celda2[1] or chr(ord(celda1[1]) - 1) == celda2[1])
