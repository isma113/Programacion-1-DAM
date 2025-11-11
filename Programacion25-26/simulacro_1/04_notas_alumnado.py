# Notas por rangos. Repite hasta escribir 'exit' como nombre. (sin and/or/not/listas/booleanos)
while 1 == 1:
    nombre = input("Nombre del alumno (o 'exit' para terminar): ")
    if nombre == "exit":
        break
    nota = int(input("Nota (0-100): "))
    while (nota < 0) or (nota > 100):
        print("Valor fuera de rango. Intente de nuevo.")
        nota = int(input("Nota (0-100): "))

    if nota >= 90:
        print(nombre, "-> Sobresaliente")
    else:
        if nota >= 70:
            print(nombre, "-> Notable")
        else:
            if nota >= 60:
                print(nombre, "-> Bien")
            else:
                if nota >= 50:
                    print(nombre, "-> Suficiente")
                else:
                    print(nombre, "-> Suspenso")
