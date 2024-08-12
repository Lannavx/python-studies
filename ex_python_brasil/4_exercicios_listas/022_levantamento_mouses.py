'''Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, 
para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera; necessita de limpeza; necessita troca do cabo ou conector; quebrado ou inutilizado. Uma identificação igual a zero encerra o programa. 
Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%'''


# Define as possíveis situações dos mouses
situacoes = ['necessita da esfera', 'necessita de limpeza', 'necessita troca do cabo ou conector', 'quebrado ou inutilizado']
quantidade_mouses = [] # Lista para armazenar as quantidades de mouses em cada situação

quantidade_situacao = len(situacoes) 

print('Informe a quantidade de mouses em cada situação. Zero encerra o programa.\n')

# Loop principal para coleta de dados
while True:

    # Itera sobre cada situação para coletar a quantidade de mouses em cada uma delas
    for i in range(quantidade_situacao):
        entrada = int(input(f'{i+1} - {situacoes[i]}: '))

        if entrada == 0:
            break

        quantidade_mouses.append(entrada)
        
    if entrada == 0:
        break    

total_mouse = sum(quantidade_mouses)
entrada_quantidade_mouse = len(quantidade_mouses)

# Verifica se há alguma quantidade de mouse registrada
if quantidade_mouses:    
    print(f'\nQuantidade de mouses: {total_mouse}\n')
    print('Situação' + ' ' * 30 + 'Quantidade' + ' ' * 5 + 'Percentual')

    # Itera sobre as entradas para calcular e exibir o percentual de cada situação
    for i in range(entrada_quantidade_mouse):
            percentual = (quantidade_mouses[i] / total_mouse) * 100   
            print(f'{i+1} - {situacoes[i]:<40} {quantidade_mouses[i]:<10} {percentual:.0f}%')
else:
    print('Não foi informado uma quantidade de mouses')
