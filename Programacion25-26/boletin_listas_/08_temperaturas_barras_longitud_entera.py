# Lee 12 temperaturas. Para cada mes, imprime: (numero_mes, longitud_barra_entera, temperatura)
temperaturas = []
indice = 0
while indice < 12:
    lectura = float(input())
    temperaturas.append(lectura)
    indice = indice + 1

indice = 0
while indice < 12:
    numero_mes = indice + 1
    longitud_barra = int(temperaturas[indice])
    print(numero_mes, longitud_barra, temperaturas[indice])
    indice = indice + 1
