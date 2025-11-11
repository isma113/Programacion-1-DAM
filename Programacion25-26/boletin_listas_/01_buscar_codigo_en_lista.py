# Lee cantidad y lista de códigos (enteros). Luego lee un código objetivo y
# muestra 1 si está en la lista y 0 si no.
codigo_lista = []
indice = 0
cantidad = int(input())
while indice < cantidad:
    codigo = int(input())
    codigo_lista.append(codigo)
    indice = indice + 1

codigo_objetivo = int(input())

encontrado_flag = 0
indice = 0
tamano = len(codigo_lista)
while indice < tamano:
    if codigo_lista[indice] == codigo_objetivo:
        encontrado_flag = 1
    indice = indice + 1

print(encontrado_flag)  # 1 = está, 0 = no está
