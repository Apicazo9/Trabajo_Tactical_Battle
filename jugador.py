from clases_personajes import Medico
from clases_personajes import Artillero
from clases_personajes import Francotirador
from clases_personajes import Inteligencia
from utils import mover
class Jugador:
    def __init__(self):
        self.oponente = None
        self.equipo = []
        self.informe = ""

    def turno(self) -> bool:
        return Artillero.vida_actual == 0 and Francotirador.vida_actual == 0

    def realizar_accion(contador, num_accion) -> str:
        frase_mover = 'Indica las coordenadas de la celda donde quieres moverte: '
        frase_disparar = 'Indica las coordenadas de la esquina superior izquierda en la que disparar (área 2x2): '
        if contador == 0:
            if num_accion == 1:
                celda = input(frase_mover)
                Medico.mover(celda)
            elif num_accion == 2:
                celda = input(frase_mover)
                Artillero.mover(celda)
            elif num_accion == 3:
                celda = input(frase_disparar)
                artillero.habilidad(celda)
            elif num_accion == 4:
                celda = input(frase_mover)
                Francotirador.mover(celda)
            elif num_accion == 5:
                celda = input(frase_disparar)
                artillero.habilidad(celda)
            elif num_accion == 6:
                celda = input(frase_mover)
                Inteligencia.mover(celda)
            elif num_accion == 7:
                celda = input('Indica las coordenadas de la esquina superior izquierda de la zona de observación (área 2x2):')
                inteligencia.habilidad(celda)
        else:
            if num_accion == 1:
                celda = input(frase_mover)
                Medico.mover(celda)
            elif num_accion == 2:
                celda = input('Indica las coordenadas de la celda en la que curar: ')
                medico.habilidad(celda)
            elif num_accion == 3:
                celda = input(frase_mover)
                Artillero.mover(celda)
            elif num_accion == 4:
                celda = input(frase_disparar)
                artillero.habilidad(celda)
            elif num_accion == 5:
                celda = input(frase_mover)
                Francotirador.mover(celda)
            elif num_accion == 6:
                celda = input(frase_disparar)
                artillero.habilidad(celda)
            elif num_accion == 7:
                celda = input(frase_mover)
                Inteligencia.mover(celda)
            elif num_accion == 8:
                celda = input('Indica las coordenadas de la esquina superior izquierda de la zona de observación (área 2x2):')
                inteligencia.habilidad(celda)

    def recibir_accion(str) -> None / dict():
    def crear_equipo(self):
        self.equipo.append(Medico())
        self.equipo.append(Artillero())
        self.equipo.append(Francotirador())
        self.equipo.append(Inteligencia())
    def posicionar_equipo(self, posicion, num_personaje):
    #num_personaje: medico(0), artillero(1), francotirador(2), inteligencia(3)
        self.equipo[num_personaje].posicion = posicion

    def set_oponente(self, jugador):
        self.oponente = jugador



