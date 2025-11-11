# 03: Estaciones del año según número de mes (match)
mes = int(input("Introduce un número de mes (1-12): "))

match mes:
    case 12 | 1 | 2:
        print("Invierno")
    case 3 | 4 | 5:
        print("Primavera")
    case 6 | 7 | 8:
        print("Verano")
    case 9 | 10 | 11:
        print("Otoño")
    case _:
        print("Mes incorrecto")
