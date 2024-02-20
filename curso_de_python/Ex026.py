'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

#Forma 1

frase = str(input('Informe uma frase qualquer: ')).strip().upper()
vezes = frase.count('A')
posicao_1 = frase.find('A')
posicao_2 = frase.rfind('A')
print(f'A letra A aparece {vezes} vezes na frase')
print(f'A primeira posição da letra A é {posicao_1+1} e a última é {posicao_2+1}')

#Forma 2

frase = str(input('Informe uma frase qualquer: ')).strip().upper()
print(f'A letra A aparece {frase.count('A')} vezes na frase')
print(f'A primeira posição da letra A é {frase.find('A')+1} e a última é {frase.rfind('A')+1}')