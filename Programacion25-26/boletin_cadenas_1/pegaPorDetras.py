# pegaPorDetras: añade un dígito por detrás.
numero = input("Número: ").strip()
digito = input("Dígito a pegar por detrás: ").strip()
if len(digito) == 0:
    print(numero)
else:
    print(numero + digito[0])
