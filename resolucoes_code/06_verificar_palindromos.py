"""
Vamos testar se uma palavra é um palíndromo.
"""

import unicodedata

# 1. Entrada do usuário
texto = input("Digite uma palavra ou frase: ")

# 2. Tudo minúsculo
texto = texto.lower()

# 3. Tirar acentos (ex.: á -> a, ã -> a)
texto = unicodedata.normalize("NFD", texto)
texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')

# 4. Deixar só letras e números
limpo = ''.join(c for c in texto if c.isalnum())

# 5. Comparar com o inverso
if limpo == limpo[::-1]:
    print("É palíndromo!")
else:
    print("Não é palíndromo.")

# -------------------------------------

"""
P/ TESTAR:

🔠 Palavras

"arara"         → palíndromo
"radar"         → palíndromo
"reviver"       → palíndromo
"cachorro"      → não é palíndromo
"computador"    → não é palíndromo

📝 Frases

"Aí, ó! O íA"                               → palíndromo (com acentos e pontuação, mas o código ignora isso)
"Socorram-me, subi no ônibus em Marrocos"   → palíndromo clássico em português
"Anotaram a data da maratona"               → palíndromo
"Hoje é sexta-feira"                        → não é palíndromo
"Eu gosto de programação"                   → não é palíndromo

"""





