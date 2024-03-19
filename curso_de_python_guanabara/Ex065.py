'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


condicao = ''
total = 0
soma = 0
maior = menor = 0
while condicao != 'N':
    numero = int(input('Informe um número qualquer: '))  
    condicao = input('Quer continuar a informar mais números? [S/N]: ').upper().strip()[0]
    total += 1
    soma += numero 
    # O primeiro número é, ao mesmo tempo, o maior e o menor valor inserido.
    if total == 1:
        maior = menor = numero
    else:
        #Para iterações subsequentes, se o número atual for maior que o maior número registrado, atualiza o maior
        if numero > maior:
            maior = numero
        #Para iterações subsequentes, se o número atual for menor que o menor número registrado, atualiza o menor
        if numero < menor:
            menor = numero        
media = soma / total
print(f'Foram informados {total} números e a média entre eles é de {media:.2f} ')
print(f'O maior valor informado foi {maior} e o menor foi {menor}')