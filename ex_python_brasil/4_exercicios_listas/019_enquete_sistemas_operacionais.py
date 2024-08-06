'''Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.'''


# Lista com os sistemas operacionais e contagem inicial de votos
lista_sistemas = [
    ['Windows Server', 0],
    ['Unix', 0],
    ['Linux', 0],
    ['Netware', 0],
    ['Mac OS', 0],
    ['Outro', 0],
]

votos_computados = 0
sistema_mais_votado = [0,0,0] # Estrutura para armazenar informações do sistema mais votado

# Exibe as opções voto para o usuário
print('''Sistemas:
1 - Windows Server
2 - Unix
3 - Linux
4 - Netware
5 - Mac OS
6 - Outro''')

# Loop principal para coleta dos votos
while True:

    enquete = int(input('Qual o melhor Sistema Operacional para uso em servidores (Pressione 0 para sair)?'))
    
    if enquete == 0:
        break

    if enquete not in range(1, 7):
        print('Opção inválida! Digite um número válido entre 1 e 6.')
        continue    
    
    # Incrementa o contador de votos para o sistema escolhido
    lista_sistemas[enquete-1][1] += 1

    votos_computados += 1

# Cabeçalho
print('\nSistema Operacional' + ' ' * 9 + 'Votos' + ' ' * 5 + '%')
print('-' * 23 + ' ' * 5 + '-' * 5 + ' ' * 5 + '-' * 3)

# Loop para exibição dos resultados de cada sistema
for sistema in lista_sistemas:

    percentual_votos = (sistema[1] / votos_computados) * 100

    # Exibe os resultados formatados para cada sistema
    print(f'{sistema[0]:<20} {sistema[1]:>10} {percentual_votos:>8.0f}%')
    
    # Adiciona o percentual à lista do sistema para uso futuro
    sistema.append(percentual_votos)

    if sistema[1] > sistema_mais_votado[1]:
        sistema_mais_votado = sistema

# Rodapé
print('-' * 23 + ' ' * 5 + '-' * 5)
print(f'Total{votos_computados:>26}')
print(f'\nO Sistema Operacional mais votado foi o {sistema_mais_votado[0]}, com {sistema_mais_votado[1]} votos, correspondendo a {sistema_mais_votado[2]:.0f}% dos votos.')