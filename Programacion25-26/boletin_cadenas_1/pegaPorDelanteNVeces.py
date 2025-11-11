# pegaPorDelanteNVeces: lee número, dígito y cuántas veces repetir por el principio.
base = input("Número base: ").strip()
digito = input("Dígito a repetir por delante: ").strip()
veces = int(input("Número de veces: "))
prefijo = ""
i = 0
while i < veces:
    if len(digito) > 0:
        prefijo = prefijo + digito[0]
    i = i + 1
print(prefijo + base)
