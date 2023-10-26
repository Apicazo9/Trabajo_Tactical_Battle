from utils import validar_celda, validar_celda_contigua

# Dimensiones tablero
max_raw = 4
max_col = 'd'

class Personaje:
    def __init__(self, nombre, vida, rango, posicion):
            self.nombre = nombre
            self.vida_maxima = vida
            self.vida_actual = vida
            self.posicion = posicion
            self.enfriamiento = 0
            self.rango = rango
    def mover(self, celda_nueva, max_col, max_row):
        col = celda_nueva[0]
        row = celda_nueva[1]
        if validar_celda(celda_nueva, max_col, max_row) and validar_celda_contigua(col, row):
            self.posicion = celda_nueva
        return None
    def curar_personaje(self, personaje):
        pass
    def disparo_unitario(self, casilla):
        pass
    def disparo_area(self, casilla):
        pass
    def explorar_area(self, casilla):
        pass