# quitaPorDetras: quita n dígitos por la derecha.
numero = input("Número: ").strip()
n = int(input("n a quitar (por detrás): "))
if n <= 0:
    print(numero)
elif n >= len(numero):
    print("")
else:
    print(numero[:-n])
