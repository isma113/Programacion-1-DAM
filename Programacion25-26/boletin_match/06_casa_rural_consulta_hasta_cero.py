# 06: Casa Rural - consulta repetida hasta introducir 0 (match + while)
print("Habitaciones: 101, 102, 201, 202, 301 (0 para salir)")

hab = int(input("Número de habitación: "))
while hab != 0:
    match hab:
        case 101:
            print("Planta: 1, Camas: 2")
        case 102:
            print("Planta: 1, Camas: 3")
        case 201:
            print("Planta: 2, Camas: 2")
        case 202:
            print("Planta: 2, Camas: 4")
        case 301:
            print("Planta: 3, Camas: 1")
        case _:
            print("Habitación no encontrada")
    hab = int(input("Número de habitación (0 para salir): "))
print("Fin")
