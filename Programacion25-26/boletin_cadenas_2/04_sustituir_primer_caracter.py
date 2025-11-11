# 04_sustituir_primer_caracter.py
# Pide una cadena y dos caracteres; sustituye la PRIMERA aparición del primero por el segundo.

input_text = input("Cadena: ")
old_char = input("Carácter a buscar: ")
new_char = input("Carácter de reemplazo: ")

position = -1
if len(old_char) > 0:
    position = input_text.find(old_char[0])

if position == -1:
    print(input_text)
else:
    left_part = input_text[:position]
    right_part = input_text[position+1:]
    print(left_part + new_char[:1] + right_part)
