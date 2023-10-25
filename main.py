from utils import limpiar_terminal
from jugador import Jugador

def validar_entrada(texto):
    texto = texto.lower()
    return texto[0] in 'abcd' and texto[1] in '1234'
def pedir_posicion(tipo):
    while True:
        pos = input(f"Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al {tipo}: ")
            if validar_entrada(pos):
                return pos
            else:
                print(f'Ups... valor de celda incorrecta.')

#def informe(contador):
    #print('---- SITUACION DEL EQUIPO ----\n')
    #print('Medico está en ', )

personajes = [
    (j1.Medico, 'Medico'),
    (j1.Artillero, 'Artillero'),
    (j1.Francotirador, 'Francotirador'),
    (j1.Inteligencia, 'Inteligencia')
]

def main():
    print('Bienvenidos a Tactical Battle. A jugar!\n')
    input('Turno del Jugador 1. Pulsa intro para comenzar')
    print("Vamos a posicionar a nuestros personajes en el tablero!")
    j1 = Jugador()
    pos_medicoj1 = pedir_posicion("Médico")
    pos_artilleroj1 = pedir_posicion("Artillero")
    pos_francotiradorj1 = pedir_posicion("Francotirador")
    pos_inteligenciaj1 = pedir_posicion("Inteligencia")

    print('Posicionamiento terminado')

    input('Jugador 1, pulsa terminar tu turno')
    limpiar_terminal()

    input('Turno del Jugador 2. Pulsa intro para comenzar')
    j2 = Jugador()
    pos_medicoj2 = pedir_posicion("Médico")
    pos_artilleroj2 = pedir_posicion("Artillero")
    pos_francotiradorj2 = pedir_posicion("Francotirador")
    pos_inteligenciaj2 = pedir_posicion("Inteligencia")

    print('Posicionamiento terminado')

    input('Jugador 2, pulsa terminar tu turno')
    limpiar_terminal()

    j1.set_oponente(j2)
    j2.set_oponente(j1)

    final = False
    while not final:
        contador = 0

        input('Turno del Jugador 1. Pulsa intro para comenzar')
        final = j1.turno()
        if final:
            print("***** El jugador 1 ha ganado la partida! *****")
            return 0
        else:

            for personaje, nombre in personajes:
                print(f'{nombre} está en {personaje.posicion} [Vida {personaje.vida_actual} ]')

            if contador == 0:
                print("1: Mover (Medico)")
                print("2: Mover (Artillero)")
                print("3: Disparar en área (2x2). Daño 1. (Artillero)")
                print("4: Mover (Francotirador)")
                print("5: Disparar a una celda. Daño 3. (Francotirador)")
                print("6: Mover (Inteligencia)")
                print("7: Revelar a los enemigos en un área 2x2. (Inteligencia)")
            else:
                print("1: Mover (Medico)")
                print("2: Curar a un compañero (Medico) ")
                print("2: Mover (Artillero)")
                print("3: Disparar en área (2x2). Daño 1. (Artillero)")
                print("4: Mover (Francotirador)")
                print("5: Disparar a una celda. Daño 3. (Francotirador)")
                print("6: Mover (Inteligencia)")
                print("7: Revelar a los enemigos en un área 2x2. (Inteligencia)")

            num_accion = input('Selecciona la acción de este turno: ')
            j1.realizar_accion(num_accion, contador)

        input('Jugador 1, pulsa intro para terminar tu turno')
        limpiar_terminal()

        input('Turno del Jugador 2. Pulsa intro para comenzar')
        final = j2.turno()
        if final:
            print("***** El jugador 2 ha ganado la partida! *****")
            return 0

        input('Jugador 2, pulsa intro para terminar tu turno')
        limpiar_terminal()

        contador += 1
if __name__ == '__main__':
    main()