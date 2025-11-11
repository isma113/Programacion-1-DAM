# Ejercicio 2 (b): igual que 2a + contar entradas (incluye el 0)
print("Introduce números. Termina con 0.")
primero = 1
creciente = 1
decreciente = 1
conteo = 0

ant = 0
n = int(input("Número: "))
while 1 == 1:
    conteo = conteo + 1
    if n == 0:
        break
    if primero == 1:
        ant = n
        primero = 0
    else:
        if ant < n:
            if decreciente == 1:
                decreciente = 0
        else:
            if ant > n:
                if creciente == 1:
                    creciente = 0
            else:
                if creciente == 1:
                    creciente = 0
                if decreciente == 1:
                    decreciente = 0
        ant = n
    n = int(input("Número: "))

if primero == 1:
    print("desordenados")
else:
    if creciente == 1:
        if decreciente == 0:
            print("creciente")
        else:
            print("desordenados")
    else:
        if decreciente == 1:
            print("decreciente")
        else:
            print("desordenados")
print("Total de valores introducidos (incluye el 0):", conteo)
print("fin")
