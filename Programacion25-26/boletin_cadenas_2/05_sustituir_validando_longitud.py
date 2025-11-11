# 05_sustituir_validando_longitud.py
# Igual que el 04, pero valida que ambos caracteres sean de longitud 1.

source_text = input("Cadena: ")

search_char = ""
while True:
    search_char = input("Carácter a buscar (1 char): ")
    if len(search_char) == 1:
        break

replace_char = ""
while True:
    replace_char = input("Carácter de reemplazo (1 char): ")
    if len(replace_char) == 1:
        break

pos = source_text.find(search_char)
if pos == -1:
    print(source_text)
else:
    print(source_text[:pos] + replace_char + source_text[pos+1:])
