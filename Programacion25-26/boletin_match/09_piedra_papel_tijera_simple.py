# 09: Piedra, papel o tijera con match (una jugada)
import random

# Entrada usuario
u = input("Elige: PIEDRA, PAPEL o TIJERA: ")
u = u.upper()

# Máquina
m_num = random.randint(0, 2)
match m_num:
    case 0:
        m = "PIEDRA"
    case 1:
        m = "PAPEL"
    case 2:
        m = "TIJERA"

print("Máquina:", m)

# Resultado
if u == m:
    print("Empate")
else:
    match (u, m):
        case ("PIEDRA", "TIJERA") | ("PAPEL", "PIEDRA") | ("TIJERA", "PAPEL"):
            print("Ganas tú")
        case ("PIEDRA", "PAPEL") | ("PAPEL", "TIJERA") | ("TIJERA", "PIEDRA"):
            print("Gana la máquina")
        case _:
            print("Entrada no válida")
