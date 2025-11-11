# 04: Repite pedir dos números y mostrar su suma hasta que ambos sean 0
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
while not (a == 0 and b == 0):
    print("Suma =", a + b)
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
print("Fin del programa.")
