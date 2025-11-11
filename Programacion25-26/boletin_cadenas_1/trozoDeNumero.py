# trozoDeNumero: devuelve el trozo de numero entre posiciones [ini..fin] (ambas incluidas).
numero = input("Número: ").strip()
ini = int(input("Posición inicial (0..): "))
fin = int(input("Posición final (>= inicial): "))
if ini < 0 or fin < 0:
    print("rango inválido")
elif ini > fin:
    print("rango inválido")
elif fin >= len(numero):
    print("rango inválido")
else:
    print(numero[ini:fin+1])
