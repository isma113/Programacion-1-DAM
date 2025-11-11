# Ejercicio 2 (a): secuencia hasta 0 -> creciente / decreciente / desordenados
print("Introduce números. Termina con 0.")
primero = 1         # 1 = aún no hay anterior; 0 = ya hay
creciente = 1       # 1 = posible creciente; 0 = ya no
decreciente = 1     # 1 = posible decreciente; 0 = ya no

ant = 0
n = int(input("Número: "))
while n != 0:
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
print("fin")
