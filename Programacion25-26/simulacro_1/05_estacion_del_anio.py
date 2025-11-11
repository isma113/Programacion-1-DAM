# Estación del año sin and/or/not/listas/booleanos
while 1 == 1:
    d = int(input("Día: "))
    m = int(input("Mes (1-12): "))
    if d > 31:
        if m > 12:
            break

    hemi = input("Hemisferio (Norte/Sur): ")
    # Validación sin and/or/not: repetir hasta que sea 'Norte' o 'Sur'
    while 1 == 1:
        ok = 0
        if hemi == "Norte":
            ok = 1
        if ok == 0:
            if hemi == "Sur":
                ok = 1
        if ok == 1:
            break
        print("Valor incorrecto. Introduce 'Norte' o 'Sur'.")
        hemi = input("Hemisferio (Norte/Sur): ")

    estacion = ""

    if hemi == "Norte":
        if m == 9:
            if d >= 23:
                estacion = "Otoño"
            else:
                estacion = "Verano"
        else:
            if m == 12:
                if d >= 21:
                    estacion = "Invierno"
                else:
                    estacion = "Otoño"
            else:
                if m == 3:
                    if d >= 21:
                        estacion = "Primavera"
                    else:
                        estacion = "Invierno"
                else:
                    if m == 6:
                        if d >= 21:
                            estacion = "Verano"
                        else:
                            estacion = "Primavera"
                    else:
                        if m == 10:
                            estacion = "Otoño"
                        else:
                            if m == 11:
                                estacion = "Otoño"
                            else:
                                if m == 1:
                                    estacion = "Invierno"
                                else:
                                    if m == 2:
                                        estacion = "Invierno"
                                    else:
                                        if m == 4:
                                            estacion = "Primavera"
                                        else:
                                            if m == 5:
                                                estacion = "Primavera"
                                            else:
                                                if m == 7:
                                                    estacion = "Verano"
                                                else:
                                                    if m == 8:
                                                        estacion = "Verano"
    else:
        if m == 9:
            if d >= 23:
                estacion = "Primavera"
            else:
                estacion = "Invierno"
        else:
            if m == 12:
                if d >= 21:
                    estacion = "Verano"
                else:
                    estacion = "Primavera"
            else:
                if m == 3:
                    if d >= 21:
                        estacion = "Otoño"
                    else:
                        estacion = "Verano"
                else:
                    if m == 6:
                        if d >= 21:
                            estacion = "Invierno"
                        else:
                            estacion = "Otoño"
                    else:
                        if m == 10:
                            estacion = "Primavera"
                        else:
                            if m == 11:
                                estacion = "Primavera"
                            else:
                                if m == 1:
                                    estacion = "Verano"
                                else:
                                    if m == 2:
                                        estacion = "Verano"
                                    else:
                                        if m == 4:
                                            estacion = "Otoño"
                                        else:
                                            if m == 5:
                                                estacion = "Otoño"
                                            else:
                                                if m == 7:
                                                    estacion = "Invierno"
                                                else:
                                                    if m == 8:
                                                        estacion = "Invierno"

    print("Estación:", estacion)
