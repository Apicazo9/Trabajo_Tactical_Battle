from utils import limpiar_terminal
from jugador import Jugador

def validar_entrada(texto):
    texto = texto.lower()
    return texto[0] in 'abcd' and texto[1] in '1234'
def pedir_posicion(tipo, posiciones):
    while True:
        pos = input(f"Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al {tipo}: ")
        if validar_entrada(pos):
            if pos not in posiciones:
                return pos
            else:
                print('Ups... la celda ya está ocupada!')
        else:
            print(f'Ups... valor de celda incorrecta.')

posiciones = []
def main():
    print('Bienvenidos a Tactical Battle. A jugar!\n')
    input('Turno del Jugador 1. Pulsa intro para comenzar\n')
    print("Vamos a posicionar a nuestros personajes en el tablero!\n")

    j1 = Jugador()

    posiciones.append(pedir_posicion('medico', posiciones))
    posiciones.append(pedir_posicion('artillero', posiciones))
    posiciones.append(pedir_posicion('francotirador', posiciones))
    posiciones.append(pedir_posicion('inteligencia', posiciones))

    j1.crear_equipo()
    j1.posicionar_equipo(posiciones)
    print('Posicionamiento terminado')

    input('Jugador 1, pulsa terminar tu turno')
    limpiar_terminal()

    input('Turno del Jugador 2. Pulsa intro para comenzar')
    j2 = Jugador()

    posiciones[:] = []

    posiciones.append(pedir_posicion('medico', posiciones))
    posiciones.append(pedir_posicion('artillero', posiciones))
    posiciones.append(pedir_posicion('francotirador', posiciones))
    posiciones.append(pedir_posicion('inteligencia', posiciones))

    j2.crear_equipo()
    j2.posicionar_equipo(posiciones)

    print('Posicionamiento terminado')

    input('Jugador 2, pulsa terminar tu turno')
    limpiar_terminal()

    j1.set_oponente(j2)
    j2.set_oponente(j1)

    final = False
    while not final:
        contador = 0

        input('Turno del Jugador 1. Pulsa intro para comenzar \n')
        final = j1.turno()
        if final:
            print("***** El jugador 1 ha ganado la partida! *****")
            return 0
        else:
            print('----SITUACION DEL EQUIPO----')
            print(j1.situacion_equipo(0))
            print(j1.situacion_equipo(1))
            print(j1.situacion_equipo(2))
            print(j1.situacion_equipo(3), '\n')
            #for personaje, nombre in personajes:
                #print(f'{nombre} está en {personaje.posicion} [Vida {personaje.vida_actual} ]')

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
                print("2: Curar a un compañero (Medico)")
                print("3: Mover (Artillero)")
                print("4: Disparar en área (2x2). Daño 1. (Artillero)")
                print("5: Mover (Francotirador)")
                print("6: Disparar a una celda. Daño 3. (Francotirador)")
                print("7: Mover (Inteligencia)")
                print("8: Revelar a los enemigos en un área 2x2. (Inteligencia)")

            num_accion = input('Selecciona la acción de este turno: ')

            j1.realizar_accion(contador, num_accion)
            #if (contador == 0 and (num_accion == 3 or num_accion == 5)) or (contador > 0 and (num_accion == 4 or num_accion == 6)):
                #j2.recibir_accion(realizar_accion)
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

