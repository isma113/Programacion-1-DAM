# Conjunto de operaciones con listas sin usar strings en runtime.

# Elemento de índice 6 (séptimo elemento) en una lista base de 7 enteros
dias_numericos = [1,2,3,4,5,6,7]
print(dias_numericos[6])

# 5 enteros aleatorios entre 0 y 8
import random
lista_aleatoria = []
indice = 0
while indice < 5:
    numero_aleatorio = random.randint(0,8)
    lista_aleatoria.append(numero_aleatorio)
    indice = indice + 1
print(lista_aleatoria)

# 20 primeros múltiplos de 3
multiplos_3_20 = []
indice = 1
while indice <= 20:
    valor = 3 * indice
    multiplos_3_20.append(valor)
    indice = indice + 1
print(multiplos_3_20)

# Añadir tres códigos [2,3,4] al final (elemento a elemento)
cola_codigos = [2,3,4]
indice = 0
tamano_cola = len(cola_codigos)
while indice < tamano_cola:
    multiplos_3_20.append(cola_codigos[indice])
    indice = indice + 1
print(multiplos_3_20)

# Generar 10 múltiplos de 3
multiplos_3_10 = []
indice = 1
while indice <= 10:
    valor = 3 * indice
    multiplos_3_10.append(valor)
    indice = indice + 1
print(multiplos_3_10)

# Insertar valor marcador 999 en posición 8
multiplos_3_10.insert(8, 999)
print(multiplos_3_10)
