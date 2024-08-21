'''Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F'''

# Solicita ao usuário que digite seu nome
nome = input('Digite seu nome: ').strip().upper()

# Imprime o nome na vertical em formato de escada invertida
for i in range(len(nome), 0, -1):
    print(nome[:i])
