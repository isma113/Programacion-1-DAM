# 11: Piedra, papel o tijera - hasta 3 victorias de alguien
import random

tu = 0
maquina = 0

while tu < 3 and maquina < 3:
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

    if u == m:
        print("Empate. Marcador:", tu, "-", maquina)
    else:
        match (u, m):
            case ("PIEDRA", "TIJERA") | ("PAPEL", "PIEDRA") | ("TIJERA", "PAPEL"):
                tu = tu + 1
                print("Ganas esta ronda. Marcador:", tu, "-", maquina)
            case ("PIEDRA", "PAPEL") | ("PAPEL", "TIJERA") | ("TIJERA", "PIEDRA"):
                maquina = maquina + 1
                print("Gana la máquina esta ronda. Marcador:", tu, "-", maquina)
            case _:
                print("Entrada no válida")

if tu == 3:
    print("¡Victoria! Marcador final:", tu, "-", maquina)
else:
    print("Gana la máquina. Marcador final:", tu, "-", maquina)
