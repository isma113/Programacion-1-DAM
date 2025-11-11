# 08: Suma los dígitos de un número (usa while)
n = int(input("Introduce un número: "))
if n < 0:
    n = -n
suma = 0
if n == 0:
    suma = 0
else:
    while n > 0:
        suma = suma + (n % 10)
        n = n // 10
print("Suma de dígitos =", suma)
