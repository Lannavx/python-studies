''' Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.'''

# Inicia um loop que continuará enquanto o usuário quiser realizar simulações
continuar = 'S'

while continuar == 'S':
    try:
        # Solicita ao usuário as populações iniciais e verifica se são válidas
        populacao_a = float(input('Informe a população do país A: '))
        populacao_b = float(input('Informe a população do país B: '))

        if populacao_a <= 0 or populacao_b <= 0: 
            print("As populações devem ser maiores que zero.")
            continue

        # Solicita ao usuário as taxas de crescimento anuais e verifica se são válidas      
        taxa_crescimento_a = float(input('Informe a taxa de crescimento anual do país A (%): '))
        taxa_crescimento_b = float(input('Informe a taxa de crescimento anual do país B (%): '))

        if taxa_crescimento_a <= 0 or taxa_crescimento_b <= 0:
            print("As taxas devem ser maiores que zero.")
            continue

        # Continua o cálculo enquanto a população de A for menor que B    
        cont_anos = 0
        while populacao_a < populacao_b:
            # Calcula o crescimento anual das populações
            populacao_a += populacao_a * (taxa_crescimento_a / 100)
            populacao_b += populacao_b * (taxa_crescimento_b / 100)
            # Incrementa o contador de anos
            cont_anos += 1
        
        # Exibe o resultado do cálculo
        print(f'São necessários {cont_anos} anos para a população do país A ultrapassar ou se igualar ao país B!')
        print('-' * 40)

    # Captura erro se a entrada não for um número e pede nova entrada    
    except ValueError:
        print("Por favor, digite um número válido.")
    
    # Pergunta ao usuário se deseja realizar outra simulação
    continuar = input("Deseja realizar outra simulação? (S/N): ").strip().upper()

print('Obrigada por usar o programa! Até breve!')