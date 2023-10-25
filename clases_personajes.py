from utils import validar_celda, validar_celda_contigua
import tablero

# Dimensiones tablero
max_raw = 4
max_col = 'd'

class Personaje:
    def __init__(self, vida, danyo, posicion, enfriamiento, habilidad, rango):
        self.vida_actual = vida
        self.vida_maxima = vida
        self.danyo = danyo
        self.posicion = posicion
        self.enfriamiento = enfriamiento
        self.habilidad = habilidad
        self.rango = rango

    def mover(self, celda_nueva, max_col, max_row):
        col = celda_nueva[0]
        row = celda_nueva[1]
        if validar_celda(celda_nueva, max_col, max_row) and validar_celda_contigua(col, row):
            self.posicion = celda_nueva
        return None

class Medico(Personaje):
    def curar_personaje(self, casilla):
        if validar_celda(casilla, max_col, max_raw):
             tablero.tablero[casilla].vida_actual = tablero.tablero[casilla].vida_maxima
class Francotirador(Personaje):
    def disparo_unitario(self, casilla):
        if validar_celda(casilla, 'd', 4):
            tablero.tablero[casilla].vida_actual = 0
        else:
            print("No puedes disparar a este objetivo.")
class Artillero(Personaje):
    def disparo_area(self, casilla):
        adjacentes = [(casilla[0] + casilla[1]), (chr(ord(casilla[0]) + 1) + casilla[1]), (casilla[0] + chr(ord(casilla[1]) + 1)), (chr(ord(casilla[0]) + 1) + chr(ord(casilla[1]) + 1))]
        for adj in adjacentes:
            if validar_celda(adj, 'd', 4):
                if isinstance(tablero.tablero[adj], Personaje):
                    tablero.tablero[adj].vida_actual -= 1
class Inteligencia(Personaje):
    def explorar_area(self, casilla):
        adjacentes = [str(casilla[0] + casilla[1]), (chr(ord(casilla[0]) + 1) + casilla[1]), (casilla[0] + chr(ord(casilla[1]) + 1)), (chr(ord(casilla[0]) + 1) + chr(ord(casilla[1]) + 1))]
        for adj in adjacentes:
            if validar_celda(adj, 'd', 4):
                print(tablero.tablero[adj])
            else:
                print('Fuera de rango')

medico = Medico(3, 0, 'a1', 1, 'curar personaje', 'no militar')
inteligencia = Inteligencia(3, 0, 'c1', 1, 'explorar area', 'no militar')
artillero = Artillero(3, 1, 'd3', 1, 'disparo area', 'militar')
francotirador = Francotirador(3, 3, 'c4', 1, 'disparo unitario', 'militar')
tablero.tablero['a1'] = medico
tablero.tablero['c1'] = inteligencia
tablero.tablero['d3'] = artillero
tablero.tablero['c4'] = francotirador


francotirador.disparo_unitario('a1')
print(medico.vida_actual)
medico.curar_personaje('a1')
print(medico.vida_actual)

inteligencia.explorar_area('a1')
artillero.disparo_area('a1')
print(medico.vida_actual)

mover_celda_contigua('a1', 'a2')
inteligencia.explorar_area('a1')