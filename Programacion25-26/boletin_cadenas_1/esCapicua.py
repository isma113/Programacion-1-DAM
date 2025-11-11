# esCapicua: imprime 'verdadero' si el número es capicúa; 'falso' en caso contrario.
numero = input("Número: ").strip()
# Ignorar signo si lo hubiera
if len(numero) > 0 and numero[0] == '-':
    numero_sin_signo = numero[1:]
else:
    numero_sin_signo = numero

# Construir la cadena invertida SIN usar [::-1]
invertida = ""
i = len(numero_sin_signo) - 1
while i >= 0:
    invertida = invertida + numero_sin_signo[i]
    i = i - 1

if numero_sin_signo == invertida:
    print("verdadero")
else:
    print("falso")
