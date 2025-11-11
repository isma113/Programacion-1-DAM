arboles = []
opcion = ''

while opcion != 'e':
    print("===== MENÚ =====")
    print("a) Introducir el número de árboles")
    print("b) Mostrar resumen de los datos")
    print("e) Salir")
    opcion = input("Elija una opción: ")

    if opcion == 'a':
        n = int(input("¿Cuántos árboles desea introducir?: "))
        for i in range(n):
            print("Árbol número", i + 1)
            tipo = input("Tipo del árbol (A o B): ")
            diametro = float(input("Diámetro del tronco (cm): "))
            altura = float(input("Altura (m): "))
            if tipo.upper() == 'B':
                edad = float(input("Edad (años): "))
                arboles.append(['B', diametro, altura, edad])
            else:
                arboles.append(['A', diametro, altura])
        print("Datos guardados correctamente.\n")

    elif opcion == 'b':
        if len(arboles) == 0:
            print("No hay datos introducidos.\n")
        else:
            print("===== RESUMEN DE ÁRBOLES =====")
            for i in range(len(arboles)):
                datos = arboles[i]
                if datos[0] == 'A':
                    print("Árbol", i + 1, ": Tipo A - Diámetro:", datos[1], "cm - Altura:", datos[2], "m")
                else:
                    print("Árbol", i + 1, ": Tipo B - Diámetro:", datos[1], "cm - Altura:", datos[2], "m - Edad:", datos[3], "años")
            print()

    elif opcion == 'e':
        print("Saliendo del programa...")

    else:
        print("Opción no válida.")
