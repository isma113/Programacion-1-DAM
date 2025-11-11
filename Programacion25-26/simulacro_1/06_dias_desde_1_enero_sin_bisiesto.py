# Días desde 1 de enero (sin bisiesto), sin listas y sin hardcodear sumas largas.
d = int(input("Día: "))
m = int(input("Mes (1-12): "))
y = int(input("Año: "))

# Acumular con bucle: para cada mes anterior a m, sumar días de ese mes.
suma = 0
i = 1
while i < m:
    dm = 0
    if i == 1:
        dm = 31
    else:
        if i == 2:
            dm = 28
        else:
            if i == 3:
                dm = 31
            else:
                if i == 4:
                    dm = 30
                else:
                    if i == 5:
                        dm = 31
                    else:
                        if i == 6:
                            dm = 30
                        else:
                            if i == 7:
                                dm = 31
                            else:
                                if i == 8:
                                    dm = 31
                                else:
                                    if i == 9:
                                        dm = 30
                                    else:
                                        if i == 10:
                                            dm = 31
                                        else:
                                            if i == 11:
                                                dm = 30
                                            else:
                                                dm = 31
    suma = suma + dm
    i = i + 1

suma = suma + d
print("Días transcurridos desde 1 de enero:", suma)
