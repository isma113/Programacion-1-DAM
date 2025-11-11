# Rota a la derecha una lista de 15 enteros en 1 posición.
vector = []
indice = 0
while indice < 15:
    valor = int(input())
    vector.append(valor)
    indice = indice + 1

ultimo_valor = vector[len(vector)-1]
indice = len(vector) - 1
while indice > 0:
    vector[indice] = vector[indice - 1]
    indice = indice - 1
vector[0] = ultimo_valor

print(vector)
