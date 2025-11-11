# 06: Igual que el anterior pero alterna filas interiores entre ###... y @* @* ... (usa for)
# n=5:
# *###*
# *@*@*
# *###*
# *@*@*
# *###*
n = int(input("Tamaño del patrón: "))
if n < 2:
    print("El número debe ser >= 2")
else:
    # superior
    print("*" + "#" * (n - 2) + "*")
    # interior alternando
    for fila in range(n - 2):
        if fila % 2 == 0:
            interior = "#" * (n - 2)
        else:
            interior = ""
            for col_int in range(n - 2):
                if col_int % 2 == 0:
                    interior = interior + "@"
                else:
                    interior = interior + "*"
        print("*" + interior + "*")
    # inferior
    print("*" + "#" * (n - 2) + "*")
