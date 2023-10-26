from utils import validar_celda, validar_celda_contigua

# Dimensiones tablero
max_raw = 4
max_col = 'd'
class Personaje:
    def __init__(self, vida, rango, posicion):
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
class Medico(Personaje):
    def __init__(self, posicion):
        super().__init__(1, 'no militar', posicion)
    def curar_personaje(self, personaje):
        pass
class Artillero(Personaje):
    def __int__(self, posicion):
        super().__init__(2, 'militar', posicion)
    def disparo_area(self, casilla):
class Francotirador(Personaje):
    def __int__(self, posicion):
        super().__init__(3, 'militar', posicion)
    def disparo_unitario(self, casilla):
        pass
class Inteligencia(Personaje):
    def __int__(self, posicion):
        super().__init__(3, 'militar', posicion)
    def explorar_area(self, casilla):
        pass