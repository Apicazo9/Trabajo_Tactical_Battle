def limpiar_terminal():
    print(chr(27) + "[2J")

# comprobar si una posicion es valida
def validar_celda (celda, max_col, max_row) -> bool:
    return (celda[0] >= 'a' and celda[0] <= max_col) and (celda[1] >= '1' and celda[1] <= str(max_row))

# comprobar celda contigua
def validar_celda_contigua(celda_actual, celda_nueva):
    return (chr(ord(celda_actual[0]) + 1) == celda_nueva[0] or chr(ord(celda_actual[0]) - 1) == celda_nueva[0]) or (chr(ord(celda_actual[1]) + 1) == celda_nueva[1] or chr(ord(celda_actual[1]) - 1) == celda_nueva[1])
def personajes_en_area(celda, personajes):
    personajes_afectados = []

    for personaje in personajes:
        if personaje.posicion == celda:
            personajes_afectados.append(personaje)

    return personajes_afectados

#si da algun problema revisa mayusculas y minusculas
def devolver_area(celda):
    col = celda[0]
    row = int(celda[1])

    if col == 'd' and row < 4:
        return [celda, col + str(row + 1)]
    elif col == 'd' and row == 4:
        return [celda]
    elif row == 4:
        codigo_unicode = ord(col)
        sig_col = chr(codigo_unicode + 1)
        return [celda, sig_col + str(row)]
    else:
        celda1 = col + str(row + 1)
        codigo_unicode = ord(col)
        sig_col = chr(codigo_unicode + 1)
        sig_row = int(row + 1)
        celda2 = sig_col + str(row)
        celda3 = sig_col + str(sig_row)
        return [celda, celda1, celda2, celda3]
def celda_ocupada(equipo, celda):
    for personaje in equipo:
        if personaje.posicion == celda:
            return True
    return False
def personaje_en_celda(celda):
    pass
