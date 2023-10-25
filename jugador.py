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
        if contador == 0:
            if num_accion == 1:
                celda = input('Indica las coordenadas de la celda donde quieres moverte: ')
                Medico.mover(celda)
            elif num_accion == 2:
                celda = input('Indica las coordenadas de la celda donde quieres moverte: ')
            elif num_accion == 3:
            elif num_accion == 4:
            elif num_accion == 5:
            elif num_accion == 6:
            elif num_accion == 7:
        else:
            if num_accion == 1:

            elif num_accion ==2:


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



