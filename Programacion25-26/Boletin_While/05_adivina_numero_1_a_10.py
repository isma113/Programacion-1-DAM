# 05: Juego de adivinar un número aleatorio del 1 al 10 usando while
import random
secreto = random.randint(1, 10)
acierto = False

while not acierto:
    intento = int(input("Adivina el número (1-10): "))
    if intento == secreto:
        print("¡Correcto! Era", secreto)
        acierto = True
    else:
        print("No es ese. Intenta de nuevo.")
