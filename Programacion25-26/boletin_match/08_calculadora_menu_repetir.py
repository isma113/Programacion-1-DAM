# 08: Calculadora con menú que se repite hasta @
op = ""

while op != "@":
    print("========================================")
    print("		CALCULADORA")
    print("========================================")
    print("	Introduzca + si desea sumar")
    print("	Introduzca - si desea restar")
    print("	Introduzca * si desea multiplicar")
    print("	Introduzca / si desea dividir")
    print("	Introduzca @ para salir del menú.")
    print("========================================")
    op = input("Opción: ")

    match op:
        case "+":
            a = float(input("Introduzca un número: "))
            b = float(input("Introduzca otro número: "))
            print("Resultado =", a + b)
        case "-":
            a = float(input("Introduzca un número: "))
            b = float(input("Introduzca otro número: "))
            print("Resultado =", a - b)
        case "*":
            a = float(input("Introduzca un número: "))
            b = float(input("Introduzca otro número: "))
            print("Resultado =", a * b)
        case "/":
            a = float(input("Introduzca un número: "))
            b = float(input("Introduzca otro número: "))
            print("Resultado =", a / b)
        case "@":
            print("Saliendo...")
        case _:
            print("Opción no válida")
