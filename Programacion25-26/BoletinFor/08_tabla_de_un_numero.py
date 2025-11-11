# 08 Tabla de multiplicar del número leído (1 al 10)
n = int(input("Introduce un número para su tabla: "))
for i in range(1, 11):
    print(i, "x", n, "=", i * n)
