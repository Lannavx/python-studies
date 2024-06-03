# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


n = int(input('Informe quantos termos deseja na sequência de Fibonacci: '))

# Inicializa as duas primeiras posições 
termo1, termo2 = 1, 1

print('-' * 25)
print('Sequência de Fibonacci:')

# Inicializa o contador 
contagem_termos = 1

# Verifica se o usuário quer pelo menos um termo
if n >= 1:
    print(termo1, end=' ')

# Continua a sequência enquanto a contagem de termos for menor que n
while contagem_termos < n:
    
    # Exibe o próximo termo
    print(termo2, end=' ')
    
    # Atualiza as variáveis para o próximo termo
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    
    # Incrementa o contador de termos
    contagem_termos += 1
