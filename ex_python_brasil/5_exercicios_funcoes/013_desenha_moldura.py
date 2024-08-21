'''Desenha moldura. 
Construa uma função que desenhe um retângulo usando os caracteres + , − e | . 
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.'''

def desenhar_moldura(linhas, colunas):
    '''Desenha um retângulo usando caracteres especiais ( +, -, | )'''

    # Garante que os valores estão dentro dos limites permitidos
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    
    # Desenha a linha superior
    print('+' + ('-' * (colunas - 2)) + '+')
    
    # Desenha as linhas do meio, se houver
    for _ in range(linhas - 2):
        print('|' + (' ' * (colunas - 2)) + '|')
    
    # Desenha a linha inferior, se houver mais de uma linha
    if linhas > 1:
        print('+' + ('-' * (colunas - 2)) + '+')

# Solicita ao usuário valores para linhas e colunas
linhas = int(input('Informe um valor para linhas: '))    
colunas = int(input('Informe um valor para colunas: '))     

# Exibe a moldura
desenhar_moldura(linhas, colunas)
