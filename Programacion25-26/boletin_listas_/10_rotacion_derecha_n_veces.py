# Rota a la derecha n veces una lista de 15 enteros. Valida que n < longitud.
vector = []
indice = 0
while indice < 15:
    valor = int(input())
    vector.append(valor)
    indice = indice + 1

rotaciones = int(input())
while rotaciones >= len(vector):
    rotaciones = int(input())

contador_rotacion = 0
while contador_rotacion < rotaciones:
    ultimo_valor = vector[len(vector)-1]
    indice = len(vector) - 1
    while indice > 0:
        vector[indice] = vector[indice - 1]
        indice = indice - 1
    vector[0] = ultimo_valor
    contador_rotacion = contador_rotacion + 1

print(vector)
