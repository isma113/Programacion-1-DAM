# Genera 20 números aleatorios (0..100), sus cuadrados y cubos. Imprime en 3 columnas.
import random
columna_numero = []
columna_cuadrado = []
columna_cubo = []

indice = 0
while indice < 20:
    valor = random.randint(0,100)
    columna_numero.append(valor)
    indice = indice + 1

indice = 0
while indice < 20:
    cuadrado = columna_numero[indice] * columna_numero[indice]
    columna_cuadrado.append(cuadrado)
    indice = indice + 1

indice = 0
while indice < 20:
    cubo = columna_numero[indice] * columna_numero[indice] * columna_numero[indice]
    columna_cubo.append(cubo)
    indice = indice + 1

indice = 0
while indice < 20:
    print(columna_numero[indice], columna_cuadrado[indice], columna_cubo[indice])
    indice = indice + 1
