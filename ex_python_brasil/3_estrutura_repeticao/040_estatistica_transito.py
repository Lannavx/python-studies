'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

# Número de cidades a serem analisadas
NUM_CIDADES = 5

# Inicializa variáveis para encontrar o maior e menor índice de acidentes
maior_indice = 0
menor_indice = float('inf')
codigo_cidade_maior_indice = codigo_cidade_menor_indice = 0

# Variáveis para calcular as médias
soma_veiculos = 0
soma_acidentes = 0
contador_cidades_menos_2000 = 0

# Loop para processar dados de cada cidade
for i in range(NUM_CIDADES):
    codigo_cidade = int(input(f'Informe o código da {i + 1}ª cidade: '))
    num_veiculos = int(input('Informe o número de veículos de passeio: '))
    num_acidentes = int(input('Informe o número de acidentes de trânsito com vítimas: '))

    # Acumula o total de veículos para calcular a média
    soma_veiculos += num_veiculos
    
    # Verifica se o número atual de acidentes é o maior ou menor registrado e atualiza as variáveis 
    if num_acidentes > maior_indice:
        maior_indice = num_acidentes
        codigo_cidade_maior_indice = codigo_cidade

    if  num_acidentes < menor_indice:
        menor_indice = num_acidentes
        codigo_cidade_menor_indice = codigo_cidade    

    # Acumula dados de acidentes para cidades com menos de 2000 veículos
    if num_veiculos < 2000:
        contador_cidades_menos_2000  += 1
        soma_acidentes += num_acidentes
        
# Calcula a média de veículos em todas as cidades    
media_total = soma_veiculos / NUM_CIDADES

# Calcula a média de acidentes para cidades com menos de 2000 veículos
if contador_cidades_menos_2000 > 0:
    media_acidente = soma_acidentes / contador_cidades_menos_2000
else:
    media_acidente = 0


print()

# Exibe os resultados
print(f'''O maior índice de acidentes de transito é {maior_indice} na cidade do código {codigo_cidade_maior_indice}. 
Enquanto que o menor índice de acidentes de transito é {menor_indice} na cidade do código {codigo_cidade_menor_indice}. ''')    
print(f'A média de veículos nas cinco cidades juntas é de {media_total:.2f}')    
print(f'A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de {media_acidente:.2f}')