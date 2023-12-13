'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5: 
    print(f'Sua média foi de {media:.1f}. Logo, você está reprovado!')
elif 7 > media >= 5:   
    print(f'Sua média foi de {media:.1f}. Logo, você está de recuperação!')
else:
    print(f'Sua média foi de {media:.1f}. Logo, você está aprovado!')  