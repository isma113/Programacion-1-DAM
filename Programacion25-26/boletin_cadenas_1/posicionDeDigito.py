# posicionDeDigito: primera ocurrencia de un dígito dentro de un número. Si no está, -1.
numero = input("Número: ").strip()
digito = input("Dígito a buscar (un carácter): ").strip()
if len(digito) == 0:
    print("-1")
else:
    pos = numero.find(digito[0])
    print(pos)
