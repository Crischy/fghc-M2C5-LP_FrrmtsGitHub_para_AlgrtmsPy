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










