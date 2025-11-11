# 20 aleatorios 0..100; pares primero e impares después usando listas auxiliares.
import random
lista_original = []
indice = 0
while indice < 20:
    numero = random.randint(0,100)
    lista_original.append(numero)
    indice = indice + 1

lista_pares = []
lista_impares = []
indice = 0
tamano = len(lista_original)
while indice < tamano:
    if (lista_original[indice] % 2) == 0:
        lista_pares.append(lista_original[indice])
    else:
        lista_impares.append(lista_original[indice])
    indice = indice + 1

lista_reordenada = []
indice = 0
while indice < len(lista_pares):
    lista_reordenada.append(lista_pares[indice])
    indice = indice + 1
indice = 0
while indice < len(lista_impares):
    lista_reordenada.append(lista_impares[indice])
    indice = indice + 1

print(lista_original)
print(lista_reordenada)
