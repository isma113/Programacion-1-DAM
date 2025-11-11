# quitaPorDelante: quita n dígitos por la izquierda.
numero = input("Número: ").strip()
n = int(input("n a quitar (por delante): "))
if n <= 0:
    print(numero)
elif n >= len(numero):
    print("")
else:
    print(numero[n:])
