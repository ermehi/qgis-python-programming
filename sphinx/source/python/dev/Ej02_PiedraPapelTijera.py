"""
Escribe un programa que simunle n partidas del juego “piedra – papel – tijera".
En cada partida se deben calcular aleatoriamente las 2 opciones (una de cada jugador) y resolver la partida de acuerdo con las reglas del juego.
Al acabar, se mostrarán los porcentajes de victorias obtenidas por cada jugador.
"""
from random import randint

PIEDRA = 1
PAPEL = 2
TIJERA = 3


num_partidas = int(input("Dame número de partidas a simular: "))

cont_partidas_ganadas_jugador_1 = 0
cont_partidas_ganadas_jugador_2 = 0
cont_partidas_empatadas = 0

for i in range(num_partidas):
    print("Partida ", i + 1)
    opc_jugador_1 = randint(1, 3)
    if opc_jugador_1 == PIEDRA:
        print("Jugador 1 elige PIEDRA")
    elif opc_jugador_1 == PAPEL:
        print("Jugador 1 elige PAPEL")
    else:
        print("Jugador 1 elige TIJERA")

    opc_jugador_2 = randint(1, 3)
    if opc_jugador_2 == PIEDRA:
        print("Jugador 2 elige PIEDRA")
    elif opc_jugador_2 == PAPEL:
        print("Jugador 2 elige PAPEL")
    else:
        print("Jugador 2 elige TIJERA")

    if opc_jugador_1 == opc_jugador_2:
        print("Empate")
        cont_partidas_empatadas += 1
    elif opc_jugador_1 == PIEDRA and opc_jugador_2 == PAPEL:
        print("Gana jugador 2")
        cont_partidas_ganadas_jugador_2 += 1
    elif opc_jugador_1 == PIEDRA and opc_jugador_2 == TIJERA:
        print("Gana jugador 1")
        cont_partidas_ganadas_jugador_1 += 1
    elif opc_jugador_1 == PAPEL and opc_jugador_2 == PIEDRA:
        print("Gana jugador 1")
        cont_partidas_ganadas_jugador_1 += 1
    elif opc_jugador_1 == PAPEL and opc_jugador_2 == TIJERA:
        print("Gana jugador 2")
        cont_partidas_ganadas_jugador_2 += 1
    elif opc_jugador_1 == TIJERA and opc_jugador_2 == PAPEL:
        print("Gana jugador 1")
        cont_partidas_ganadas_jugador_1 += 1
    elif opc_jugador_1 == TIJERA and opc_jugador_2 == PIEDRA:
        print("Gana jugador 2")
        cont_partidas_ganadas_jugador_2 += 1

porcentaje_partidas_ganadas_jugador_1 = (cont_partidas_ganadas_jugador_1 / num_partidas) * 100
porcentaje_partidas_ganadas_jugador_2 = (cont_partidas_ganadas_jugador_2 / num_partidas) * 100
porcentaje_partidas_empatadas = (cont_partidas_empatadas / num_partidas) * 100

print("Porcentaje de partidas ganadas por el jugador 1: ", porcentaje_partidas_ganadas_jugador_1)
print("Porcentaje de partidas ganadas por el jugador 2: ", porcentaje_partidas_ganadas_jugador_2)
print("Porcentaje de partidas empatadas: ", porcentaje_partidas_empatadas)