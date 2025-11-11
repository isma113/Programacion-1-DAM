# 01 Contar: imprime del 1 al número leído (debe ser > 0)
n = int(input("Introduce un número mayor que 0: "))
while n <= 0:
    n = int(input("Debe ser mayor que 0. Inténtalo de nuevo: "))

for i in range(1, n + 1):
    print(i)
