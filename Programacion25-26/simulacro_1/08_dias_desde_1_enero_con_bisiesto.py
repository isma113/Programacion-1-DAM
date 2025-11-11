# Días desde 1 de enero con bisiesto (sin listas, sin hardcodear sumas, sin operadores lógicos)
d = int(input("Día: "))
m = int(input("Mes (1-12): "))
y = int(input("Año: "))

# ¿Año bisiesto?
b = 0
if y % 400 == 0:
    b = 1
else:
    if y % 4 == 0:
        if y % 100 != 0:
            b = 1

feb = 28
if b == 1:
    feb = 29

suma = 0
i = 1
while i < m:
    dm = 0
    if i == 1:
        dm = 31
    else:
        if i == 2:
            dm = feb
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
