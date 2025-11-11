# 03_primera_y_ultima_mayus.py
# Cambia primera y última letra de cada palabra a mayúsculas, resto minúsculas.

input_name = input("Nombre y apellidos: ").strip()
name_words = input_name.split()

output_text = ""
index_word = 0
while index_word < len(name_words):
    word = name_words[index_word]
    if len(word) == 0:
        transformed = ""
    elif len(word) == 1:
        transformed = word.upper()
    else:
        first_upper = word[0].upper()
        last_upper = word[len(word)-1].upper()
        middle_lower = ""
        index_inner = 1
        while index_inner < len(word) - 1:
            middle_lower = middle_lower + word[index_inner].lower()
            index_inner = index_inner + 1
        transformed = first_upper + middle_lower + last_upper
    if index_word > 0:
        output_text = output_text + " "
    output_text = output_text + transformed
    index_word = index_word + 1

print(output_text)
