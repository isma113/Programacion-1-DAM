# Ejercicio 2 (c): igual que 2b + media (sin contar el 0)
print("Introduce números. Termina con 0.")
primero = 1
creciente = 1
decreciente = 1
conteo_total = 0
suma_valores = 0
conteo_valores = 0

ant = 0
n = int(input("Número: "))
while 1 == 1:
    conteo_total = conteo_total + 1
    if n == 0:
        break
    suma_valores = suma_valores + n
    conteo_valores = conteo_valores + 1

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

print("Total de valores introducidos (incluye el 0):", conteo_total)
if conteo_valores > 0:
    media = suma_valores / conteo_valores
    print("Media (sin contar el 0):", media)
else:
    print("Media (sin contar el 0): 0")
print("fin")
