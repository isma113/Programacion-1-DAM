# Lee 10 enteros a una lista; luego imprime la lista y después los elementos en orden inverso.
valores = []
indice = 0
while indice < 10:
    numero = int(input())
    valores.append(numero)
    indice = indice + 1

print(valores)

indice = len(valores) - 1
while indice >= 0:
    print(valores[indice])
    indice = indice - 1
