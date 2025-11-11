# 02_iniciales_mayus.py
# Pide nombre y apellidos, muestra las iniciales en mayúsculas (sin separadores).

full_name = input("Nombre y apellidos: ").strip()
name_parts = full_name.split()

result_initials = ""
index_part = 0
while index_part < len(name_parts):
    word = name_parts[index_part]
    if len(word) > 0:
        result_initials = result_initials + word[0].upper()
    index_part = index_part + 1

print(result_initials)
