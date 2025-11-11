# 06_miles_con_puntos.py
# Recibe una cadena numérica y la devuelve con separaciones de miles por puntos.
# Gestiona el signo '-' si existe.

raw_number = input("Número entero: ").strip()

sign_prefix = ""
if len(raw_number) > 0 and raw_number[0] == '-':
    sign_prefix = "-"
    raw_number = raw_number[1:]

grouped_result = ""
digit_counter = 0
index_char = len(raw_number) - 1

while index_char >= 0:
    current_digit = raw_number[index_char]
    grouped_result = current_digit + grouped_result
    digit_counter = digit_counter + 1
    if digit_counter == 3 and index_char != 0:
        grouped_result = "." + grouped_result
        digit_counter = 0
    index_char = index_char - 1

print(sign_prefix + grouped_result)
