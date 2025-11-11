# 07: Calculadora simple con match (una sola operación)
op = input("Operador (+,-,*,/): ")
a = float(input("Introduzca un número: "))
b = float(input("Introduzca otro número: "))

match op:
    case "+":
        print("Resultado =", a + b)
    case "-":
        print("Resultado =", a - b)
    case "*":
        print("Resultado =", a * b)
    case "/":
        print("Resultado =", a / b)
    case _:
        print("Operador no válido")
