'''Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 
Calcule e mostre:
a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
considerando que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. 
A disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.'''

import random

DISTANCIA = 1000
VALOR_GASOLINA = 2.25


modelos_carros = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeout']
random.shuffle(modelos_carros) # Embaralha a lista de carros
quantidade_carros = len(modelos_carros)
 
# Gera valores aleatoriamente com base na quantidade de carros
consumo = [random.uniform(1,20) for _ in range(quantidade_carros)]

# Lista para armazenar os dados de cada carro, incluindo litros necessários e custo
dados_carro = []

print('Comparativo de Consumo de Combustível\n')

# Exibe os dados dos veiculos e calcula o consumo e custo para cada carro
for i in range(quantidade_carros):
    print(f'Veiculo {i + 1}')
    print(f'Nome: {modelos_carros[i]}')  
    print(f'Km por litro: {consumo[i]:.1f}')        

    
    litros = DISTANCIA / consumo[i]
    valor_gasolina_percorrida = litros * VALOR_GASOLINA

    # Armazena os dados calculados
    dados_carro.append([litros, modelos_carros[i], valor_gasolina_percorrida])

print('\nRelatório Final')

# Exibe o relatório final
for i in range(quantidade_carros):
    print(f'{i+1} - ' +  f'{modelos_carros[i]:<10} -' + f'{consumo[i]:>8.1f} -' + f'{dados_carro[i][0]:>8.1f} litros - ' + f'R${dados_carro[i][2]:.2f}')
    
# Identifica e exibe o veículo com menor consumo    
veiculo_menor_consumo = min(dados_carro)
print(f'O menor consumo é do {veiculo_menor_consumo[1]}')