'''
Dicionários são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de
tipos imutáveis como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves {} ou a classe dict para criar dicionários.
'''

# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list


# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas: # Loop que itera sobre cada pergunta na lista de perguntas
    print('Pergunta:', pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opções']): # Loop que itera sobre cada opção de resposta da pergunta atual.
        print(f'{i}) {opcao}') # Imprime a opção com um índice numérico que o usuário pode usar para selecionar.
    print()
        
    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(pergunta['Opções']) # Número de opções disponíveis para a pergunta atual

    if escolha.isdigit(): # Converte a escolha do usuário para um inteiro, se for um dígito.
        escolha_int = int(escolha)

    if escolha_int is not None: # Verifica se a escolha do usuário foi convertida para inteiro com sucesso.
        if escolha_int >= 0 and escolha_int < qtd_opcoes: # Confirma se o inteiro está dentro do intervalo válido de opções.
            if pergunta['Opções'][escolha_int] == pergunta['Resposta']: # Se a opção escolhida corresponde à resposta correta, registra o acerto.
                acertou = True
    
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou! 🎉')    
    else:
        print('Errou! ❌')
    
    print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas!')        


  