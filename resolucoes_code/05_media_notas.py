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









