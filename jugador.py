from utils import personajes_en_area
from utils import devolver_area
import personajes

class Jugador:
    def __init__(self):
        self.oponente = None
        self.equipo = []
        self.informe = ""

    def turno(self) -> bool:
        return Artillero.vida_actual == 0 and Francotirador.vida_actual == 0

    def obtener_coordenadas(celda):
        # Suponiendo que 'celda' es una tupla (x, y)
        x, y = celda
        return x, y
    def personajes_en_area(celda, personajes):
        x, y = obtener_coordenadas(celda)
        personajes_afectados = []

        for personaje in personajes:
            x, y = personaje.x, personaje.y
            if (accion_x <= x < accion_x + 2) and (accion_y <= y < accion_y + 2):
                personajes_afectados.append(personaje)

        return personajes_afectados

#hace falta añadir que solo los vivos puede realizar acciones.
    def realizar_accion(self, contador, num_accion) -> str:
        frase_mover = 'Indica las coordenadas de la celda donde quieres moverte: '
        frase_disparar = 'Indica las coordenadas de la esquina superior izquierda en la que disparar (área 2x2): '
        if contador == 0:
            if num_accion == 1:
                celda = input(frase_mover)
                Medico.mover(celda)
                return ""
            elif num_accion == 2:
                celda = input(frase_mover)
                Artillero.mover(celda)
                return ""
            elif num_accion == 3:
                celda = input(frase_disparar)
                habilidad = artillero.habilidad(celda)
                return habilidad
            elif num_accion == 4:
                celda = input(frase_mover)
                Francotirador.mover(celda)
                return ''
            elif num_accion == 5:
                celda = input(frase_disparar)
                artillero.habilidad(celda)
                return habilidad
            elif num_accion == 6:
                celda = input(frase_mover)
                Inteligencia.mover(celda)
                return ''
            elif num_accion == 7:
                celda = input('Indica las coordenadas de la esquina superior izquierda de la zona de observación (área 2x2):')
                habilidad = inteligencia.habilidad(celda)
                return habilidad
        else:
            if num_accion == 1:
                celda = input(frase_mover)
                Medico.mover(celda)
                return celda
            elif num_accion == 2:
                celda = input('Indica las coordenadas de la celda en la que curar: ')
                medico.habilidad(celda)
                return celda
            elif num_accion == 3:
                celda = input(frase_mover)
                Artillero.mover(celda)
                return celda
            elif num_accion == 4:
                celda = input(frase_disparar)
                artillero.habilidad(celda)
                return celda
            elif num_accion == 5:
                celda = input(frase_mover)
                Francotirador.mover(celda)
                return celda
            elif num_accion == 6:
                celda = input(frase_disparar)
                artillero.habilidad(celda)
                return celda
            elif num_accion == 7:
                celda = input(frase_mover)
                Inteligencia.mover(celda)
                return celda
            elif num_accion == 8:
                celda = input('Indica las coordenadas de la esquina superior izquierda de la zona de observación (área 2x2):')
                inteligencia.habilidad(celda)
                return celda
    def recibir_accion(self, accion):
        inicial_personaje = accion[:1]
        celda = accion[1:]
        if inicial_personaje == 'A':
            area = devolver_area(celda)
            for personaje in self.equipo:
                for casilla in area:
                    if personaje.posicion == casilla:
                        personaje.vida_actual -= 1
                        #Habria que aclarar aqui que pasa si la vida es igual a 0
        else: #en principio solo deberían entrar por aqui acciones del franco
            for personaje in self.equipo:
                if celda == personaje.posicion:
                    personaje.vida_actual = 0
    def crear_equipo(self, posiciones):
        self.equipo.append(personajes.Medico(posiciones[0]))
        self.equipo.append(personajes.Artillero(posiciones[1]))
        self.equipo.append(personajes.Francotirador(posiciones[2]))
        self.equipo.append(personajes.Inteligencia(posiciones[3]))
    def posicionar_equipo(self, posicion, num_personaje):
    #num_personaje: medico(0), artillero(1), francotirador(2), inteligencia(3)
        self.equipo[num_personaje].posicion = posicion

    def set_oponente(self, jugador):
        self.oponente = jugador



