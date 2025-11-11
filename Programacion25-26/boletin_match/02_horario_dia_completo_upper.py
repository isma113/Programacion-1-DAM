# 02: Horario del día con upper() y match simple
dia = input("Introduce un día de la semana: ")
dia = dia.upper()

# Horarios de ejemplo muy simples
match dia:
    case "LUNES":
        print("Lunes: 8:00-14:00, 16:00-18:00")
    case "MARTES":
        print("Martes: 8:00-14:00, 16:00-18:00")
    case "MIERCOLES" | "MIÉRCOLES":
        print("Miércoles: 8:00-14:00, 16:00-18:00")
    case "JUEVES":
        print("Jueves: 8:00-14:00, 16:00-18:00")
    case "VIERNES":
        print("Viernes: 8:00-14:00")
    case "SABADO" | "SÁBADO" | "DOMINGO":
        print("Día de estudio y reflexión")
    case _:
        print("Valor incorrecto")
