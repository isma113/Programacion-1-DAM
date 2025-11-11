# 01: Horario del día lunes (match) y fines de semana
dia = input("Introduce un día de la semana: ")

if dia == "LUNES" or dia == "Lunes" or dia == "lunes":
    print("Horario Lunes: 8:00-14:00, 16:00-18:00")
elif dia == "Sábado" or dia == "SABADO" or dia == "sabado" or dia == "sábado" or dia == "DOMINGO" or dia == "Domingo" or dia == "domingo":
    print("Día de estudio y reflexión")
else:
    print("Valor incorrecto")
