''' Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
Faça um programa que calcule o valor de H com N termos.'''

# Loop infinito que continuará executando até que seja interrompido
while True:

    # Solicita ao usuário um número para determinar o número de termos da série
    termo = int(input('Informe um número inteiro e postivo (informe zero para sair): '))

    # Condição de parada do loop
    if termo == 0:
        break

    # Inicializa a soma com 1 já que o primeiro termo é 1 
    soma = 1

    # Inicia uma lista vazia para armazenar os termos como strings, começando com '1'
    termos_str = ['1']

    # Loop que itera de 2 até o número de termos desejado
    for m in range(2, termo + 1):
        numerador = 1
        denominador = m

        # Adiciona cada termo formatado como string à lista
        termos_str.append(f'{numerador}/{denominador}')

        # Calcula cada termo da série e acumula esses valores para obter a soma total dos termos da série
        divisao = numerador / denominador
        soma += divisao

    # Junta todos os termos com ' + ' entre eles
    serie_str = " + ".join(termos_str)

    # Imprime a série completa com o resultado
    print(f'H = {serie_str} = {soma:.2f}')