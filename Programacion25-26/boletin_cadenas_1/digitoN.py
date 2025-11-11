# digitoN: devuelve el dígito que está en la posición n (0-index, izquierda a derecha).
numero = input("Número: ").strip()
n = int(input("Posición (0..): "))
if n < 0 or n >= len(numero):
    print("-1")
else:
    print(numero[n])
