def limpiar_terminal():
print(chr(27) + "[2J")
def validar_celda(celda, max_col, max_row) -> bool:
# Para comprobar si una celda "B5" está dentro es una posición válida del tablero que comprende entre A1 y (max_col, max_row)
def comprobar_celda_disponible(celda, equipo) -> bool:
# Para comprobar si un miembro del equipo ya ocupa una celda dada
def validar_celda_contigua(celda1, celda2) -> bool:
# Para comprobar si la celda 1 es contigua a la celda 2