# Ejercicio 1: grupos de 3 números hasta 0 0 0 (sin and, or, not; sin listas; sin booleanos)
print("Introduce grupos de 3 números. Termina con: 0 0 0")

while 1 == 1:
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    c = int(input("Número 3: "))

    # Comprobar fin: a==0 y b==0 y c==0 sin usar and
    fin = 0
    if a == 0:
        if b == 0:
            if c == 0:
                fin = 1
    if fin == 1:
        break

    # Determinar orden
    if a < b:
        if b < c:
            print("creciente")
        else:
            if a > b:
                if b > c:
                    print("decreciente")
                else:
                    print("desordenados")
            else:
                print("desordenados")
    else:
        if a > b:
            if b > c:
                print("decreciente")
            else:
                print("desordenados")
        else:
            print("desordenados")

print("fin")
