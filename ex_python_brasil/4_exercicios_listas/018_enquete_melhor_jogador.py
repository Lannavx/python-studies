'''Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. 
Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. 
Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. 
Um número de jogador igual zero, indica que a votação foi encerrada. 
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:
a. O total de votos computadosb.;
b. Os númeos e respectivos votos de todos os jogadores que receberam votos;
c. O percentual de votos de cada um destes jogadores;
d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. 
O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. 
Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, 
obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.'''


lista_jogadores = []
votos_computados = 0
melhor_jogador = [0,0,0] # Estrutura para armazenar informações do melhor jogador

# Armazena informações dos 23 jogadores e seus votos iniciais
for num_jogador in range(1, 24):
    lista_jogadores.append([num_jogador, 0])

# Loop principal para coleta dos votos
while True:
    enquete = int(input('Quem foi o melhor entre os 23 jogadores (Pressione 0 para sair)? '))
    
    if enquete == 0:
        break

    if enquete not in range(1, 24):
        print('Opção inválida! Digite um número válido entre 1 e 23.')
        continue    
    
    # Contabiliza o voto para o jogador correspondente
    lista_jogadores[enquete-1][1] += 1
    
    votos_computados += 1

print('\nResultado da votação:')
print(f'\nForam computados {votos_computados} votos.\n')
print('Jogador' + ' ' * 3 + 'Votos' + ' ' * 10 + '%')

# Loop para exibição dos resultados de cada jogador que recebeu votos
for jogador in lista_jogadores:

    percentual_votos = (jogador[1] / votos_computados) * 100

    # Exibe os dados apenas dos jogadores que receberam votos e formatação para jogadores com número menor que 10
    if jogador[1] > 0 and jogador[0] <= 9:
        print(f'0{jogador[0]}' + ' ' * 10 + f'{jogador[1]}' + ' ' * 10 + f'{percentual_votos:.1f}%')
    elif jogador[1] > 0 and jogador[0] > 9:
        print(f'{jogador[0]}' + ' ' * 10 + f'{jogador[1]}' + ' ' * 10 + f'{percentual_votos:.1f}%')
    
    # Adiciona o percentual à lista do jogador para uso futuro
    jogador.append(percentual_votos)

    if jogador[1] > melhor_jogador[1]:
        melhor_jogador = jogador

print(f'O melhor jogador foi o número {melhor_jogador[0]}, com {melhor_jogador[1]} votos, correspondendo a {melhor_jogador[2]:.0f}% do total de votos.')