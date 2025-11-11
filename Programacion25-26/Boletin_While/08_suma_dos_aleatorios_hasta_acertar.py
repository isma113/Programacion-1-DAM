# 08: Genera dos números al azar (0..10) y pide su suma hasta acertar
import random
a = random.randint(0, 10)
b = random.randint(0, 10)
respuesta = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "? "))
while respuesta != a + b:
    print("No es correcto. Inténtalo de nuevo.")
    respuesta = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "? "))
print("¡Correcto!")
