# 03: Tabla de multiplicar (1 al 10) del número que pide por teclado, usando while
n = int(input("Número para la tabla: "))
i = 1
while i <= 10:
    print(i, "x", n, "=", i * n)
    i = i + 1
