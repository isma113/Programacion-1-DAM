# 07: Pide contraseña repetidamente hasta que sea "1234"
pwd = input("Introduce la contraseña: ")
while pwd != "1234":
    print("Incorrecta. Prueba otra vez.")
    pwd = input("Introduce la contraseña: ")
print("Bienvenido")
