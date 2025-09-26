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










