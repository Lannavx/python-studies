'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;'''

cont_acima_media = 0
cont_abaixo_sete = 0

# Lista vazia para armazenar as notas fornecidas pelo usuário
notas = []

# Loop infinito para entrada de notas
while True:
    valores = float(input('Informe uma nota qualquer ou -1 para sair do programa: '))

    # Condição de parada
    if valores == -1:
        break
        
    notas.append(valores)

quantidade_valores = len(notas)
soma_valores = sum(notas)

# Verifica se foram inseridos valores para evitar divisão por zero
if quantidade_valores > 0: 

    media_valores = soma_valores / quantidade_valores

    # Itera sobre a lista de notas para determinar contagens específicas
    for valor in notas:
        if valor > media_valores:
            cont_acima_media += 1
        if valor < 7:
            cont_abaixo_sete += 1       

     # Imprime resultados 
    print(f'A quantidade de valores lidos é: {quantidade_valores}')
    print('Valores informados:', ' '.join(map(str, notas)))
    print('Valores na ordem inversa:')
    for nota in reversed(notas):
        print(nota)
    print(f'A soma dos valores é de {soma_valores}')
    print(f'A média dos valores é de {media_valores:.2f}')
    print(f'A quantidade de valores acima da média calculada é de {cont_acima_media}')
    print(f'A quantidade de valores abaixo de sete é de {cont_abaixo_sete}')
    print('Programa encerrado, obrigado!')

else:
    print('Não foi informado nenhum valor.')