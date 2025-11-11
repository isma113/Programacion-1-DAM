# Lee 10 enteros. Imprime cada uno seguido de un código: 2 si es máximo, 1 si es mínimo, 0 en otro caso.
muestra = []
indice = 0
while indice < 10:
    numero = int(input())
    muestra.append(numero)
    indice = indice + 1

valor_maximo = muestra[0]
valor_minimo = muestra[0]
indice = 1
tamaño = len(muestra)
while indice < tamaño:
    if muestra[indice] > valor_maximo:
        valor_maximo = muestra[indice]
    if muestra[indice] < valor_minimo:
        valor_minimo = muestra[indice]
    indice = indice + 1

indice = 0
while indice < tamaño:
    etiqueta = 0
    if muestra[indice] == valor_maximo:
        etiqueta = 2
    if muestra[indice] == valor_minimo:
        if etiqueta == 2:
            etiqueta = 2
        else:
            etiqueta = 1
    print(muestra[indice], etiqueta)
    indice = indice + 1
