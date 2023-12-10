#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Informe a sua nota: '))
nota2 = float(input('Informe a sua outra nota: '))

media = (nota1 + nota2) / 2
print(f'A sua média é {media:.1f}')