# 10: Piedra, papel o tijera - repetir mientras haya empate
import random

empate = True
while empate:
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
        print("Empate. Jugamos de nuevo.")
        empate = True
    else:
        match (u, m):
            case ("PIEDRA", "TIJERA") | ("PAPEL", "PIEDRA") | ("TIJERA", "PAPEL"):
                print("Ganas tú")
                empate = False
            case ("PIEDRA", "PAPEL") | ("PAPEL", "TIJERA") | ("TIJERA", "PIEDRA"):
                print("Gana la máquina")
                empate = False
            case _:
                print("Entrada no válida")
                empate = False
