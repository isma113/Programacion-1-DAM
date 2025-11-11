# 02: Cuadrado lleno de asteriscos con espacios entre * (usa for)
n = int(input("Tamaño del cuadrado: "))
if n < 1:
    print("El número debe ser >= 1")
else:
    for fila in range(n):
        linea = ""
        for col in range(n):
            if col == 0:
                linea = "*"
            else:
                linea = linea + " *"
        print(linea)
