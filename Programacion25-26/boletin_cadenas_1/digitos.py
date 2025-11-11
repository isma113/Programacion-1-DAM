# digitos: cuenta cuántos dígitos tiene un entero (ignora signo)
texto = input("Número: ").strip()
if len(texto) > 0 and texto[0] == '-':
    texto = texto[1:]
print(len(texto))
