# pegaPorDetrasNVeces: lee número, dígito y cuántas veces repetir por el final.
base = input("Número base: ").strip()
digito = input("Dígito a repetir por detrás: ").strip()
veces = int(input("Número de veces: "))
sufijo = ""
i = 0
while i < veces:
    if len(digito) > 0:
        sufijo = sufijo + digito[0]
    i = i + 1
print(base + sufijo)
