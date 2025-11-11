# 04: Borde superior e inferior con # entre *, y filas del medio con * separados (usa for)
# Ejemplo n=5:
# *###*
# * * * * *
# * * * * *
# * * * * *
# *###*
n = int(input("Tamaño del patrón: "))
if n < 2:
    print("El número debe ser >= 2")
else:
    # fila superior
    if n == 2:
        print("**")
    else:
        print("*" + "#" * (n - 2) + "*")
    # filas intermedias
    for _ in range(n - 2):
        linea = ""
        for col in range(n):
            if col == 0:
                linea = "*"
            else:
                linea = linea + " *"
        print(linea)
    # fila inferior
    if n > 2:
        print("*" + "#" * (n - 2) + "*")
