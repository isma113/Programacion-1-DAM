# 01: Triángulo creciente de asteriscos (usa for)
n = int(input("Introduce un número (alto del triángulo): "))
if n < 1:
    print("El número debe ser >= 1")
else:
    for i in range(1, n + 1):
        print("*" * i)
