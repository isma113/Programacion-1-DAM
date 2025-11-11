# 01_frases_texto.py
# Presenta cada frase (terminada en '.') en una línea.
# Cuenta cuántas frases hay, las palabras totales y las palabras por frase.

input_text = ("La inyección de SQL es un tipo de ciberataque encubierto en el cual un hacker inserta código propio en un sitio web con el fin de quebrantar las medidas de seguridad y acceder a datos protegidos. "
              "Una vez dentro, puede controlar la base de datos del sitio web y secuestrar la información de los usuarios. "
              "Le explicamos cómo funcionan los ataques de inyección de SQL, cómo combatirlos y cómo una herramienta antivirus potente lo puede proteger contra las consecuencias.")

sentence_list = []
current_sentence = ""
index_char = 0

while index_char < len(input_text):
    current_char = input_text[index_char]
    current_sentence = current_sentence + current_char
    if current_char == '.':
        sentence_list.append(current_sentence.strip() + " ")
        current_sentence = ""
    index_char = index_char + 1

# Mostrar cada frase en su propia línea
index_sentence = 0
while index_sentence < len(sentence_list):
    print(sentence_list[index_sentence])
    index_sentence = index_sentence + 1

# Contar frases
print("Frases:", len(sentence_list))

# Contar palabras totales y por frase
total_words_count = 0
index_sentence = 0
while index_sentence < len(sentence_list):
    words_in_sentence = sentence_list[index_sentence].strip().split()
    total_words_count = total_words_count + len(words_in_sentence)
    print("Palabras en frase", index_sentence + 1, ":", len(words_in_sentence))
    index_sentence = index_sentence + 1

print("Total de palabras:", total_words_count)
