# 12: Piedra, papel o tijera - 3 partidas y preguntar si seguir si no hay ganador
import random

def resultado_ronda(u, m):
    if u == m:
        return 0
    match (u, m):
        case ("PIEDRA", "TIJERA") | ("PAPEL", "PIEDRA") | ("TIJERA", "PAPEL"):
            return 1
        case ("PIEDRA", "PAPEL") | ("PAPEL", "TIJERA") | ("TIJERA", "PIEDRA"):
            return -1
        case _:
            return 2  # entrada inválida

seguir = "S"

while seguir == "S":
    tu = 0
    maquina = 0
    partidas = 0

    while partidas < 3:
        u = input("Elige: PIEDRA, PAPEL o TIJERA: ").upper()
        m_num = random.randint(0, 2)
        match m_num:
            case 0:
                m = "PIEDRA"
            case 1:
                m = "PAPEL"
            case 2:
                m = "TIJERA"
        print("Máquina:", m)

        r = resultado_ronda(u, m)
        match r:
            case 1:
                tu = tu + 1
                print("Ganas esta ronda.")
            case -1:
                maquina = maquina + 1
                print("Gana la máquina esta ronda.")
            case 0:
                print("Empate en la ronda.")
            case 2:
                print("Entrada no válida.")
        partidas = partidas + 1

    if tu > maquina:
        print("Ganador: Tú. Marcador:", tu, "-", maquina)
        seguir = "N"
    elif maquina > tu:
        print("Ganador: Máquina. Marcador:", tu, "-", maquina)
        seguir = "N"
    else:
        print("No hay ganador tras 3 partidas. ¿Deseas seguir? (S/N)")
        seguir = input().upper()

print("Fin del juego.")
