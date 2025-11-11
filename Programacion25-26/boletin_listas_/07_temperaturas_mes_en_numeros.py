# Lee 12 temperaturas. Imprime (numero_mes, temperatura).
temperaturas = []
indice = 0
while indice < 12:
    lectura = float(input())
    temperaturas.append(lectura)
    indice = indice + 1

indice = 0
while indice < 12:
    numero_mes = indice + 1
    print(numero_mes, temperaturas[indice])
    indice = indice + 1
