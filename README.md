# Resolvendo Códigos em Python com o GitHub Copilot

Olá!! Aqui veremos algumas resoluções de códigos em python utilizando o GitHub Copilot.

### Atenção ⚠️ 

Não tem acesso ao GitHub Copilot.Não tem problema! Pode utilizar o [ChatGPT](https://chatgpt.com/) como seu copiloto de estudos...

## 1 - Concatenando Dados 🐾

Descrição:
Vamos receber dois dados diferentes do usuário e concatena-los em uma única string.

O que aprenderemos?

* Manipulação de Strings (string)
* Concatenação
* Entrada de dados
* Utilização eficiente do GitHub Copilot

### Código do Exercício:

``` Python
"""
Recebe dois dados do usuário e concatena em uma única string
"""

primeiro = input("Digite o primeiro dado: ")
segundo  = input("Digite o segundo dado: ")

# Opção A: concatenação direta (sem espaço)
resultado = primeiro + segundo
print("Resultado (sem espaço):", resultado)

# Opção B: concatenação com espaço entre os dados
resultado_com_espaco = primeiro + " " + segundo
print("Resultado (com espaço):", resultado_com_espaco)
```

<br>

## 2 - Repetindo Textos ✏️

Descrição:
Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 

O que aprenderemos?

* Manipulação de Strings (string)
* Números Inteiros (int)
* Múltiplas repetições
* Entrada de dados
* Aproveitar as sugestões do GitHub Copilot

### Código do Exercício:

``` Python
""" 
Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número 
de vezes informado.
"""

# pede ao usuário uma string e um número inteiro
s = input("Digite uma string: ")
n = int(input("Digite um número inteiro (ex.: 3): "))

# garante número positivo
if n < 0:
    n = abs(n)

# repetição normal
resultado_sem_espacos = s * n

# repetição com espaços (usa join para juntar a string com ' ')
resultado_com_espacos = (s + " ") * n

# exibe os dois resultados
print("Sem espaços:", resultado_sem_espacos)
print("Com espaços:", resultado_com_espacos)
```

<br>

## 3 - Operações Matemáticas Simples 📐

Descrição:
Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

O que aprenderemos?

* Operações Matemáticas Básicas
* Entrada de dados
* Utilização eficiente do GitHub Copilot

### Código do Exercício:

``` Python
"""
Vamos solicitar como entrada dois números e depois vamos realizar as quatro principais operações matemáticas entre eles. 
(O valor a retornar deve ser absoluto/positivo)
"""

# Peço dois números (pode usar inteiros ou decimais)
a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))

# Soma (depois aplico abs para garantir valor positivo)
soma = abs(a + b)

# Subtração (resultado absoluto)
sub = abs(a - b)

# Multiplicação (resultado absoluto)
mul = abs(a * b)

# Divisão: verifico se b é zero antes de dividir
if b != 0:
    div = abs(a / b)
else:
    div = None  # indica que não é possível dividir por zero

# Imprimir resultados
print("Soma (absoluta):", soma)
print("Subtração (absoluta):", sub)
print("Multiplicação (absoluta):", mul)
if div is None:
    print("Divisão: impossível (divisão por zero).")
else:
    print("Divisão (absoluta):", div)
```

<br>

## 4 - Verificando Números Pares e Ímpares 🧮

Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do GitHub Copilot(ou outra IA) para otimizar a estrutura do código.

O que aprenderemos?
* Utilização de condicionais em Python (if, else) para realizar verificações.
* Introdução ao conceito de operador de módulo (%) para verificar se um número é par ou ímpar.
* Exploração do uso de uma ferramenta de IA, como o GitHub Copilot, para otimizar a estrutura do código.

### Código do Exercício:

``` Python
"""
Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.
"""

# pede um número inteiro ao usuário
num = int(input("Digite um número inteiro: "))

# verifica se o resto da divisão por 2 é zero (par) ou não (ímpar)
if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")
```

<br>

## 5 - Calculando Média de Notas 📚

Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 
Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

O que aprenderemos?
* Uso de variáveis para armazenar dados fornecidos pelo usuário.
* Aplicação de operadores aritméticos (+, /) para calcular a média de um conjunto de valores.
* Prática na solicitação e manipulação de entrada do usuário.

### Código do Exercício:

``` Python
"""
Agora vamos calcular a média de três notas fornecidas na entrada do usuário.
"""

# Ler três notas do usuário (aceita vírgula ou ponto como separador decimal)
nota1 = float(input("Digite a 1ª nota: ").replace(',', '.'))
nota2 = float(input("Digite a 2ª nota: ").replace(',', '.'))
nota3 = float(input("Digite a 3ª nota: ").replace(',', '.'))

# Calcular a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Mostrar a média formatada com duas casas decimais
print(f"A média das notas é: {media:.2f}")
```

<br>

## 6 - Verificando Palíndromos 🔄

Descrição: Vamos testar se uma palavra é um palíndromo.
Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

O que aprenderemos?
* Manipulação de strings em Python, especialmente invertendo uma string.
* Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo.
* Introdução ao conceito de palíndromos e sua aplicação em problemas de programação.

### Código do Exercício:

``` Python
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

# -----------------

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
```