# 04: Estaciones con día y cambios el 20 de mar/jun/sep/dic
mes = int(input("Mes (1-12): "))
dia = int(input("Día: "))

# Por defecto, estación base por mes
estacion = ""
match mes:
    case 1 | 2:
        estacion = "Invierno"
    case 3:
        if dia <= 20:
            estacion = "Invierno"
        else:
            estacion = "Primavera"
    case 4 | 5:
        estacion = "Primavera"
    case 6:
        if dia <= 20:
            estacion = "Primavera"
        else:
            estacion = "Verano"
    case 7 | 8:
        estacion = "Verano"
    case 9:
        if dia <= 20:
            estacion = "Verano"
        else:
            estacion = "Otoño"
    case 10 | 11:
        estacion = "Otoño"
    case 12:
        if dia <= 20:
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    case _:
        estacion = "Fecha incorrecta"

print(estacion)
