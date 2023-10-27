from utils import validar_celda, validar_celda_contigua, devolver_area
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

    def habilidad(self, atacante, casilla, lista_equipo):
        if atacante == 'artillero' or atacante == 'inteligencia':
             if validar_celda(casilla, 'd', 4) and (atacante.enfriamineto == 0):
                 area = devolver_area(casilla)
                 for personaje in lista_equipo:
                     for celda in area:
                        if personaje.posicion == casilla:
                             return atacante[0] + casilla
                        else:
                            return None
        else:
            for 







class Medico(Personaje):
    def __init__(self, posicion):
        super().__init__(1, 'no militar', posicion)
    def curar_personaje(self, personaje):
        personaje.vida_actual = personaje.vida_maxima


class Artillero(Personaje):
    def __int__(self, posicion):
        super().__init__(2, 'militar', posicion)
    def disparo_area(self, personaje):
        personaje.vida_actual -= 1


class Francotirador(Personaje):
    def __int__(self, posicion):
        super().__init__(3, 'militar', posicion)
    def disparo_unitario(self, personaje):
        personaje.vida_actual = 0


class Inteligencia(Personaje):
    def __int__(self, posicion):
        super().__init__(3, 'militar', posicion)
    def explorar_area(self, personaje):
        print('El {personaje} esta en la casilla {posicion}'.format(type(personaje), personaje.posicion))

