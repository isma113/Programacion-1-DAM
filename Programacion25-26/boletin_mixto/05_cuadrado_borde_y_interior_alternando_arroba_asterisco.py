# 05: Borde con * y # (# continuo), interior alternando @ y * (usa for)
# n=5 ejemplo:
# *###*
# *@*@*
# *@*@*
# *@*@*
# *###*
n = int(input("Tamaño del patrón: "))
if n < 2:
    print("El número debe ser >= 2")
else:
    # superior
    print("*" + "#" * (n - 2) + "*")
    # interior
    for _ in range(n - 2):
        interior = ""
        # alternamos @ y * en las columnas interiores
        # col_int va de 0 a n-3
        for col_int in range(n - 2):
            if col_int % 2 == 0:
                interior = interior + "@"
            else:
                interior = interior + "*"
        print("*" + interior + "*")
    # inferior
    print("*" + "#" * (n - 2) + "*")
