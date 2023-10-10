# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# int = conversão de uma variável ou string para um número inteiro
# float = transforma um dado em um tipo flutuante, ou seja, um número com casa decimal
primeira_nota = int(input("Infome sua nota 1: "))
segunda_nota = float(input("Infome sua nota 2: "))
terceira_nota = int(input("Infome sua nota 3: "))
quarta_nota = float(input("Infome sua nota 4: "))

media_bimestral = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

# f = format = quando você usa o "f" antes de uma string, significa que você está permitindo a formatação da mesma, ou seja, usar variáveis ou alterar parâmetros.
# :.2f = formatação = define as casas após a virgula
print(f"Sua média bimestral é {media_bimestral:.1f}")

# o nome do padrão de declaração do Python (variáveis e funções) é o "SNAKE CASE"