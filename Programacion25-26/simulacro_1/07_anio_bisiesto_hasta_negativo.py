# Año bisiesto hasta negativo (sin listas/booleanos/operadores lógicos)
a = int(input("Año (negativo para terminar): "))
while a >= 0:
    b = 0
    if a % 400 == 0:
        b = 1
    else:
        if a % 4 == 0:
            if a % 100 != 0:
                b = 1
    if b == 1:
        print(a, "es bisiesto")
    else:
        print(a, "no es bisiesto")
    a = int(input("Año (negativo para terminar): "))
print("Fin")
