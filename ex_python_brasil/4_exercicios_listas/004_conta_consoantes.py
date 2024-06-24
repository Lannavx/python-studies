# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

# Lista de vogais para comparação
vogais = ['a', 'e', 'i', 'o', 'u']

# Lista para armazenar as consoantes encontradas
consoantes = []

# Solicita uma palavra ao usuário
palavra = input('Informe uma palavra de até 10 caracteres: ').strip().lower()

# Verifica se o comprimento da entrada é apropriado
if len(palavra) <= 10:
     
    # Itera sobre cada caractere em 'palavra' e adiciona à lista consoantes se não for uma vogal
    for caracter in palavra:
        if caracter not in vogais: 
            consoantes.append(caracter)    
            
    # Verifica se foram encontradas consoantes.  
    if consoantes:
        # Se sim, exibe o resultado.
        print(f'\nForam lidas {len(consoantes)} consoantes em "{palavra}".')
        print('As consoantes são:', ' '.join(consoantes))
    else:
        # Caso não, informa ao usuário
        print(f'Não foram lidas consoantes em "{palavra}". Todas as letras são vogais ou não há letras.')

else:
    print('A entrada é muito longa. Por favor, escreva algo de até 10 caracteres.')      