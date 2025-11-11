# 05: Casa Rural - muestra listado y consulta por número (match)
print("Habitaciones disponibles: 101, 102, 201, 202, 301")
print("Formato: habitación -> (planta, camas)")
print("101 -> (1ª planta, 2 camas)")
print("102 -> (1ª planta, 3 camas)")
print("201 -> (2ª planta, 2 camas)")
print("202 -> (2ª planta, 4 camas)")
print("301 -> (3ª planta, 1 cama)")

hab = int(input("Introduce número de habitación: "))

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
