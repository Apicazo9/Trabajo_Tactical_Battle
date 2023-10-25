from clases_personajes import Medico
from clases_personajes import Artillero
from clases_personajes import Francotirador
from clases_personajes import Inteligencia
class Jugador:
    def __init__(self):
        self.oponente = None
        self.equipo = []
        self.informe = ""

    def turno(self) -> bool:
        return Artillero.vida_actual == 0 and Francotirador.vida_actual == 0

    def realizar_accion() -> str:
    def recibir_accion(str) -> None / dict():
    def crear_equipo():
        self.equipo.append(Medico())
        self.equipo.append(Artillero())
        self.equipo.append(Francotirador())
        self.equipo.append(Inteligencia())
    def posicionar_equipo(posicion, num_personaje):
    #num_personaje: medico(0), artillero(1), francotirador(2), inteligencia(3)
        self.equipo[num_personaje].posicion = posicion

    def set_oponente(jugador):
        self.oponente = jugador



