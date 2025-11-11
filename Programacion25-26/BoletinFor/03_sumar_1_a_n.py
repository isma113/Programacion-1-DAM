# 03 Sumar 1..n: si n <= 0 el programa finaliza
n = int(input("Introduce n (mayor que 0): "))
if n <= 0:
    print("Finalizando.")
else:
    suma = 0
    for i in range(1, n + 1):
        suma = suma + i
    print("Suma 1..", n, "=", suma)
