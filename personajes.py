from utils import validar_celda, validar_celda_contigua, devolver_area
class Personaje:
    def __init__(self, vida, rango, posicion):
            self.vida_maxima = vida
            self.vida_actual = vida
            self.posicion = posicion
            self.enfriamiento = 0
            self.rango = rango

    def mover(self, clase, celda_nueva, max_col, max_row):
        col = celda_nueva[0]
        row = celda_nueva[1]
        if validar_celda(celda_nueva, max_col, max_row) and validar_celda_contigua(col, row):
            clase.posicion = celda_nueva
        return None
    def habilidad(self, atacante, casilla, lista_equipo):
        lista_afectados = []
        if validar_celda(casilla, 'd', 4) and (atacante.enfriamineto == 0):
            if atacante == 'artillero' or atacante == 'inteligencia':
                area = devolver_area(casilla)
                for personaje in lista_equipo:
                    for celda in area:
                        if personaje.posicion == celda:
                            lista_afectados.append(atacante[0] + casilla)
                    if len(lista_afectados) == 0:
                        return None
                    else:
                        return lista_afectados
            else:
                for personaje in lista_equipo:
                    if personaje.posicion == casilla:
                        lista_afectados.append(atacante[0] + casilla) 
                    if len(lista_afectados) == 0:
                        return None
                    else:        
                        return lista_afectados                      
        else:
            return None
            
class Medico(Personaje):
    def __init__(self, posicion):
        super().__init__(1, 'no militar', posicion)
    def curar_personaje(self, personaje):
        pass
class Artillero(Personaje):
    def __int__(self, posicion):
        super().__init__(2, 'militar', posicion)
        self.danyo = 1
    def disparo_area(self, casilla):
        pass
class Francotirador(Personaje):
    def __int__(self, posicion):
        super().__init__(3, 'militar', posicion)
        self.danyo = 3
    def disparo_unitario(self, casilla):
        pass
class Inteligencia(Personaje):
    def __int__(self, posicion):
        super().__init__(3, 'militar', posicion)
    def explorar_area(self, casilla):
        pass
