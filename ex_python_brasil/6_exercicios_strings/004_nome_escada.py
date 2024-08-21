'''Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO'''

# Solicita ao usuário que digite seu nome
nome = input('Digite seu nome: ').strip().upper()

# Imprime o nome na vertical em formato de escada
for i in range(1, len(nome) + 1):
    print(nome[:i])
