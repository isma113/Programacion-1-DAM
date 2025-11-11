# 02: Pide números hasta que el usuario ingrese 0 y muestra la suma
suma = 0
n = int(input("Introduce un número (0 para terminar): "))
while n != 0:
    suma = suma + n
    n = int(input("Introduce un número (0 para terminar): "))
print("Suma total =", suma)
