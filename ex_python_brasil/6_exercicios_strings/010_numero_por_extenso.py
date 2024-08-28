# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

def numero_por_extenso(numero):
    '''Converte um número inteiro em sua forma por extenso'''
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dez_a_dezenove = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

    # Se o número for menor que 10, retorna o nome correspondente na lista 'unidades'
    if numero < 10:
        return unidades[numero]
    # Se o número estiver entre 10 e 19, retorna o nome correspondente na lista 'dez_a_dezenove'
    elif 10 <= numero < 20:
        return dez_a_dezenove[numero - 10] # Subtrai 10 para alinhar o número com o índice correto da lista
    # Para números de 20 a 99
    else:
        dezena = numero // 10
        unidade = numero % 10
        # Se a unidade for 0, retorna apenas o nome da dezena
        if unidade == 0: 
            return dezenas[dezena]
        else:
            return f'{dezenas[dezena]} e {numero_por_extenso(unidade)}'


# Solicita o número ao usuário
numero = int(input('Digite um número entre 0 e 99: '))

# Verifica se o número está dentro do intervalo válido
if 0 <= numero <= 99: 
    print(f'O número {numero} por extenso é {numero_por_extenso(numero)}')
else:
    print('Número fora do intervalo permitido.')
