'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

nota_um = float(input('Informe a sua primeira nota: '))
nota_dois = float(input('Informe a sua segunda nota: '))
nota_tres = float(input('Informe a sua terceira nota: '))

media = (nota_um + nota_dois + nota_tres) / 3

if media == 10:
    print(f'Sua média foi {media:.2f}. Você foi APROVADO COM DISTINÇÃO!')
elif media < 7:
    print(f'Sua média foi {media:.2f}. Você foi REPROVADO!')
else:
    print(f'Sua média foi {media:.2f}. Você foi APROVADO!')
