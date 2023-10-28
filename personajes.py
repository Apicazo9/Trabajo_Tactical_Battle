from utils import validar_celda, validar_celda_contigua, devolver_area
class Personaje:
    def __init__(self, vida, rango, nombre):
        self.nombre = nombre
        self.vida_maxima = vida
        self.vida_actual = vida
        self.posicion = ""
        self.enfriamiento = 0
        self.rango = rango
        self.max_col = 'd'
        self.max_row = 4

    def mover(self, celda_nueva):
        self.posicion = celda_nueva
        return None
    def habilidad(self):
        raise NotImplementedError
class Medico(Personaje):
    def __init__(self):
        super().__init__(1, 'no militar', 'Medico')

    def habilidad(self, personaje):
        self.curar_personaje(personaje)
        return None
    def curar_personaje(self, personaje):
        personaje.vida_actual = personaje.vida_maxima
class Artillero(Personaje):
    def __int__(self):
        super().__init__(2, 'militar', 'Artillero')
        self.danyo = 1
    def habilidad(self, celda):
        return 'A' + celda
    def disparo_area(self, personaje):
        personaje.vida_actual -= 1
class Francotirador(Personaje):
    def __int__(self):
        super().__init__(3, 'militar', 'Francotirador')
        self.danyo = 3
    def habilidad(self, celda):
        return 'F' + celda
    def disparo_unitario(self, personaje):
        personaje.vida_actual = 0
class Inteligencia(Personaje):
    def __int__(self):
        super().__init__(3, 'militar', 'Inteligencia')
    def habilidad(self, celda):
        return 'I' + celda
    def explorar_area(self, casilla):
        #print(f'El {personaje} ha sido avistado {personaje.poscion}'.format(personaje, personaje.poscion))


        '''lista_afectados = []
        if atacante.enfriamineto == 0:
            if atacante == 'Artillero' or atacante == 'Inteligencia':
                area = devolver_area(casilla)
                for personaje in lista_equipo:
                    for celda in area:
                        if personaje.posicion == celda:
                            lista_afectados.append(atacante[0] + casilla)
                    if len(lista_afectados) == 0:
                        return None
                    else:
                        return lista_afectados
            elif atacante == 'Francotirador':
                for personaje in lista_equipo:
                    if personaje.posicion == casilla:
                        lista_afectados.append(atacante[0] + casilla)
                    if len(lista_afectados) == 0:
                        return None
                    else:
                        return lista_afectados
            else:
                self.curar_personaje()
                return None
        else:
            return None'''
