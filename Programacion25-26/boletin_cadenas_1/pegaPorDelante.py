# pegaPorDelante: añade un dígito por delante.
numero = input("Número: ").strip()
digito = input("Dígito a pegar por delante: ").strip()
if len(digito) == 0:
    print(numero)
else:
    print(digito[0] + numero)
