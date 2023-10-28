import utils
import personajes

class Jugador:
    def __init__(self):
        self.oponente = None
        self.equipo = []
        self.informe = ""
    def turno(self) -> bool:
        if self.equipo[1].vida_actual == 0 and self.equipo[2].vida_actual == 0:
            return True
        else:
            return False
    def personaje_en_celda(self, celda):
        for personaje in self.equipo:
            if personaje.posicion == celda:
                return personaje
        return None
    def perdido(self):
        if self.equipo[1].vida_actual <= 0 and self.equipo[2].vida_actual <= 0:
            return True
        else:
            return False
    def situacion_equipo(self, n):
        if self.equipo[n].vida_actual == 0:
            return None
        else:
            return f"{self.equipo[n].nombre} está en {self.equipo[n].posicion} [Vida {self.equipo[n].vida_actual}/{self.equipo[n].vida_maxima}]"
#hace falta añadir que solo los vivos puede realizar acciones.
    def realizar_accion(self, contador, num_accion) -> str:
        #list_equipos -> 0: medico, 1: artillero, 2: francotirador, 3: inteligencia
        frase_disparar = 'Indica las coordenadas de la esquina superior izquierda en la que disparar (área 2x2): '
        if num_accion == '1':
            while True:
                celda = input(f"Indica la celda a la que quieres mover al Médico (posicion actual: {self.equipo[0].posicion})")
                if utils.validar_celda(celda, self.equipo[0].max_col, self.equipo[0].max_row):
                    if not utils.celda_ocupada(self.equipo, celda):
                        if utils.validar_celda_contigua(self.equipo[0].posicion, celda):
                            return self.equipo[0].mover(celda)
                        else:
                            print("Ups... la celda debe ser contigua")
                    else:
                        print("Ups... la celda está ocupada")
                else:
                    print("Ups... la celda no es válida")
        elif num_accion == '2' and contador >= 1:
            while True:
                celda = input('Indica las coordenadas de la celda en la que curar: ')
                if utils.validar_celda(celda, self.equipo[0].max_col, self.equipo[0].max_row):
                    if utils.celda_ocupada(self.equipo, celda):
                        personaje = self.personaje_en_celda(celda)
                        return self.equipo[0].habilidad(personaje)
                    else:
                        print('Ups... no hay nadie en esa celda')
                else:
                    print('Ups... la celda no es válida')

        elif (num_accion == '2' and contador == 0) or (num_accion == '3' and contador >= 1) :
            while True:
                celda = input(f"Indica la celda a la que quieres mover al Artillero (posicion actual: {self.equipo[1].posicion})")
                if utils.validar_celda(celda, self.equipo[1].max_col, self.equipo[1].max_row):
                    if not utils.celda_ocupada(self.equipo, celda):
                        if utils.validar_celda_contigua(self.equipo[1].posicion, celda):
                            return self.equipo[1].mover(celda)
                        else:
                            print("Ups... la celda debe ser contigua")
                    else:
                        print("Ups... la celda está ocupada")
                else:
                    print("Ups... la celda no es válida")
        elif (num_accion == '3' and contador == 0) or (num_accion == '4' and contador >= 1):
            celda = input(frase_disparar)
            return self.equipo[1].habilidad(celda)
        elif (num_accion == '4' and contador == 0) or (num_accion == '5' and contador >= 1):
            while True:
                celda = input(f"Indica la celda a la que quieres mover al Francotirador (posicion actual: {self.equipo[2].posicion})")
                if utils.validar_celda(celda, self.equipo[2].max_col, self.equipo[2].max_row):
                    if not utils.celda_ocupada(self.equipo, celda):
                        if utils.validar_celda_contigua(self.equipo[2].posicion, celda):
                            return self.equipo[2].mover(celda)
                        else:
                            print("Ups... la celda debe ser contigua")
                    else:
                        print("Ups... la celda está ocupada")
                else:
                    print("Ups... la celda no es válida")
        elif (num_accion == '5' and contador == 0) or (num_accion == '6' and contador >= 1):
            celda = input(frase_disparar)
            return self.equipo[2].habilidad(celda)
        elif (num_accion == '6' and contador == 0) or (num_accion == '7' and contador >= 1):
            while True:
                celda = input(f"Indica la celda a la que quieres mover a Inteligencia (posicion actual: {self.equipo[3].posicion})")
                if utils.validar_celda(celda, self.equipo[3].max_col, self.equipo[3].max_row):
                    if not utils.celda_ocupada(self.equipo, celda):
                        if utils.validar_celda_contigua(self.equipo[3].posicion, celda):
                            return self.equipo[3].mover(celda)
                        else:
                            print("Ups... la celda debe ser contigua")
                    else:
                        print("Ups... la celda está ocupada")
                else:
                    print("Ups... la celda no es válida")
        elif (num_accion == '7' and contador == 0) or (num_accion == '8' and contador >= 1):
            celda = input('Indica las coordenadas de la esquina superior izquierda de la zona de observación (área 2x2):')
            return self.equipo[3].habilidad(celda)
    def recibir_accion(self, accion):
        inicial_personaje = accion[:1]
        celda = accion[1:]
        if inicial_personaje == 'A':
            area = utils.devolver_area(celda)
            for personaje in self.equipo:
                for casilla in area:
                    if personaje.posicion == casilla:
                        personaje.vida_actual -= 1
        elif inicial_personaje == 'F': #en principio solo deberían entrar por aqui acciones del franco
            for personaje in self.equipo:
                if celda == personaje.posicion:
                    personaje.vida_actual = 0
        elif inicial_personaje == 'I':
            area = utils.devolver_area(celda)
            informe = ''
            for personaje in self.equipo:
                for casilla in area:
                    if personaje.posicion == casilla:
                        informe += 'El ' + personaje.nombre + 'ha sido avistado ' + personaje.poscion + '\n'
        estado_partida = self.perdido()
        salida = {"informe": informe, "estado": estado_partida}
        return salida
    def crear_equipo(self):
        self.equipo.append(personajes.Medico())
        self.equipo.append(personajes.Artillero(2, 'militar', 'Artillero')) #si quito los atributos da error
        self.equipo.append(personajes.Francotirador(3, 'militar', 'Francotirador'))
        self.equipo.append(personajes.Inteligencia(3, 'militar', 'Inteligencia'))
    def posicionar_equipo(self, posiciones):
        for indice, posicion in enumerate(posiciones):
            self.equipo[indice].posicion = posicion
    def set_oponente(self, jugador):
        self.oponente = jugador



