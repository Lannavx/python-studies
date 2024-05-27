'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
 O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
 se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. 
 '''

nota_um = float(input('Informe a primeira nota: '))
nota_dois = float(input('Informe a segunda nota: '))

if 0 <= nota_um <= 10 and 0 <= nota_dois <= 10:
    media = (nota_um + nota_dois) / 2

    if 0 <= media < 4:
        conceito = 'E'
        status = 'REPROVADO'
    elif 4 <= media < 6:
        conceito = 'D'
        status = 'REPROVADO'
    elif 6 <= media < 7.5:
        conceito = 'C'
        status = 'APROVADO'    
    elif 7.5 <= media < 9:
        conceito = 'B'
        status = 'APROVADO'
    elif 9 <= media <= 10:
        conceito = 'A'
        status = 'APROVADO'
    else:
        conceito = 'Inválido'
        status = 'Inválido'

    print('=' * 20)
    print(f'''
    Primeira Nota: {nota_um}
    Segunda Nota: {nota_dois}
    Média: {media:.2f}
    Conceito: {conceito}
    Status: {status}
    ''')
else:
    print('Notas inválidas. As notas devem estar entre 0 e 10.')