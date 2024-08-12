'''A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar 
os usuários com maior espaço ocupado. 
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que 
gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. 
A conversão do espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. 
O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

'''
lista_usuarios = []

# Abre o arquivo de texto com os dados dos usuários para leitura
with open('023_usuarios', 'r') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        partes = linha.strip().split() # Divide a linha em nome e número, removendo espaços extras e quebras de linha
        nome = ' '.join(partes[:-1])   # Junta novamente partes do nome que possam ter sido separadas
        numero = int(partes[-1])       # Converte a última parte em inteiro para obter o número que representa os bytes utilizados
        lista_usuarios.append([nome, numero])

# Inicializa a variável para a soma total dos dados usados por todos os usuários
soma_todos_dados = 0

# Calcula a soma total dos dados usados
for usuario in lista_usuarios:
    soma_todos_dados += usuario[1] 

def converter_byte_megabyte(byte):
    return byte * 10**-6; 

def calcular_percentual_uso(bytes_usados):
    return (bytes_usados / soma_todos_dados) * 100

# Abre um arquivo para escrita do relatório
with open('023_relatorio', 'w', encoding='UTF-8') as arquivo:

    arquivo.write('ACME Inc.' + ' ' * 10 + 'Uso do espaço em disco pelos usuários\n')
    arquivo.write('-' * 60)
    arquivo.write('\nNr.  Usuário' + ' ' *5 + 'Espaço utilizado' + ' ' * 10 + '% do uso\n\n')

    # Escreve as informações de cada usuário no arquivo
    for i in range(len(lista_usuarios)):
        arquivo.write(f'{i+1:<4} {lista_usuarios[i][0]:<10} {converter_byte_megabyte(lista_usuarios[i][1]):>10.2f} MB {calcular_percentual_uso(lista_usuarios[i][1]):>18.2f}%\n')

    # Calcula e escreve o espaço total e médio ocupado
    espaco_total_mb = converter_byte_megabyte(soma_todos_dados)
    espaco_medio_mb = espaco_total_mb / len(lista_usuarios)
    
    arquivo.write(f'\nEspaço total ocupado: {espaco_total_mb:.2f} MB\n')
    arquivo.write(f'Espaço médio ocupado: {espaco_medio_mb:.2f} MB\n')    