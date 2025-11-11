# 07: Imprime los dígitos de un número de atrás hacia adelante (usa while)
n = int(input("Introduce un número: "))
if n == 0:
    print(0)
else:
    if n < 0:
        n = -n
    while n > 0:
        print(n % 10)
        n = n // 10
