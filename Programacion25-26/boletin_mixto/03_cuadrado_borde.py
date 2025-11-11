# 03: Solo el borde del cuadrado (usa for)
n = int(input("Tamaño del cuadrado: "))
if n < 1:
    print("El número debe ser >= 1")
else:
    for fila in range(n):
        linea = ""
        for col in range(n):
            if fila == 0 or fila == n - 1 or col == 0 or col == n - 1:
                # en los bordes imprimimos *
                if col == 0:
                    linea = "*"
                else:
                    linea = linea + " *"
            else:
                # interior: espacio simple para mantener el hueco
                if col == 0:
                    linea = " "
                else:
                    linea = linea + "  "
        print(linea)
