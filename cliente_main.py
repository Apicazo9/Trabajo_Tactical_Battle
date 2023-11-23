from utils import limpiar_terminal
from jugador import Jugador
import sys
import socket
import threading

posiciones = []

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

def main():

    if len(sys.argv) != 3:
        print("Inicie el cliente con el siguiente formato: python3 cliente_main.py <IP_del_servidor> <puerto>")
        sys.exit(1)
    else:
        ip = sys.argv[1]
        puerto = int(sys.argv[2])

    print('Bienvenidos a Tactical Battle.\n')
    usuario = input('Dime tu nombre de usuario: ')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, puerto))
    print("Conectado al servidor")

    s.send(usuario.encode())
    nombre_enemigo = s.recv(1024).decode()
    print('Tu enemigo es: ', nombre_enemigo)
    datos = s.recv(1024).decode() #recibir si empieza jugando o esperando
    if datos == 'juegas':
        print('Empiezas jugando')
    else:
        print('Empiezas esperando')

    print("Vamos a posicionar a nuestros personajes en el tablero!\n")

    j1 = Jugador()

    posiciones.append(pedir_posicion('medico', posiciones))
    posiciones.append(pedir_posicion('artillero', posiciones))
    posiciones.append(pedir_posicion('francotirador', posiciones))
    posiciones.append(pedir_posicion('inteligencia', posiciones))

    j1.crear_equipo()
    j1.posicionar_equipo(posiciones)
    print('Posicionamiento terminado')

    listo = 'listo'
    s.sendall(listo.encode())
    codigo = s.recv(1024).decode()

    limpiar_terminal()

    final = False
    contador = 0
    while not final:
        input('Turno del Jugador 1. Pulsa intro para comenzar \n')
        if contador > 0:
            print('---- INFORME ----')
            print(informe)

        print('----SITUACION DEL EQUIPO----')
        j1.situacion_equipo(0)
        j1.situacion_equipo(1)
        j1.situacion_equipo(2)
        j1.situacion_equipo(3)

        if contador == 0:
            print("1: Mover (Medico)")
            print("2: Mover (Artillero)")
            print("3: Disparar en área (2x2). Daño 1. (Artillero)")
            print("4: Mover (Francotirador)")
            print("5: Disparar a una celda. Daño 3. (Francotirador)")
            print("6: Mover (Inteligencia)")
            print("7: Revelar a los enemigos en un área 2x2. (Inteligencia)")

            num_accion = input('Selecciona la acción de este turno: ')
            codigo_accion = j1.realizar_accion(contador, num_accion)
            s.sendall(codigo_accion.encode())
            recibir_acc = s.recv(1024).decode()
            if codigo_accion is not None:
                salida = s.recv(1024).decode()
                informe = salida["informe"]
                print('---- RESULTADO ACCIÓN ----')
                print(informe)

        else:
            seleccion_correcta = False
            while not seleccion_correcta:
                print("1: Mover (Medico)")
                print("2: Curar a un compañero (Medico)")
                print("3: Mover (Artillero)")
                print("4: Disparar en área (2x2). Daño 1. (Artillero)")
                print("5: Mover (Francotirador)")
                print("6: Disparar a una celda. Daño 3. (Francotirador)")
                print("7: Mover (Inteligencia)")
                print("8: Revelar a los enemigos en un área 2x2. (Inteligencia)")

                num_accion = input('Selecciona la acción de este turno: ')
                if (num_accion == '1' or num_accion == '2') and j1.equipo[0].vida_actual > 0:
                    seleccion_correcta = True
                elif (num_accion == '3' or num_accion == '4') and j1.equipo[1].vida_actual > 0:
                    seleccion_correcta = True
                elif (num_accion == '5' or num_accion == '6') and j1.equipo[2].vida_actual > 0:
                    seleccion_correcta = True
                elif (num_accion == '7' or num_accion == '8') and j1.equipo[3].vida_actual > 0:
                    seleccion_correcta = True
                else:
                    print('El personaje está muerto, escoja otra accion: \n')

            codigo_accion = j1.realizar_accion(contador, num_accion)
            if codigo_accion is not None:
                #salida = j2.recibir_accion(codigo_accion)
                informe = salida["informe"]
                estado_partida = salida["estado"]
                print('---- RESULTADO ACCIÓN ----')
                print(informe)
                if estado_partida:
                    final = True

        #final = j2.turno()
        if final:
            print("***** El jugador 1 ha ganado la partida! *****")
            return 0


        contador += 1
if __name__ == '__main__':
    main()
