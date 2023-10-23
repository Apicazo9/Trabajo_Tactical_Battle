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
        input('Turno del Jugador 1. Pulsa intro para comenzar')
        final = j1.turno()
        if final:
            print("***** El jugador 1 ha ganado la partida! *****")
            return 0

        input('Jugador 1, pulsa intro para terminar tu turno')
        limpiar_terminal()

        input('Turno del Jugador 2. Pulsa intro para comenzar')
        final = j2.turno()
        if final:
            print("***** El jugador 2 ha ganado la partida! *****")
            return 0

        input('Jugador 2, pulsa intro para terminar tu turno')
        limpiar_terminal()


if __name__ == '__main__':
    main()