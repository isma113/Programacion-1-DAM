# voltea: da la vuelta a un número (como cadena). Mantiene el signo al frente si existe. SIN usar [::-1].
texto = input("Número: ").strip()
signo = ""
if len(texto) > 0 and texto[0] == '-':
    signo = "-"
    texto = texto[1:]

invertido = ""
i = len(texto) - 1
while i >= 0:
    invertido = invertido + texto[i]
    i = i - 1

print(signo + invertido)
