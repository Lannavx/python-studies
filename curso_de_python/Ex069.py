'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos'''

print('-' * 20)
print('Cadastro de Dados')
print('-' * 20)

cont_homens = 0
cont_mulheres_menos_20 = 0
cont_mais_18 = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        print('Opção inválida! Digite M para Masculino e F para Feminino')
        sexo = input('Informe o sexo [M/F]: ').strip().upper()
    if idade >= 18:
        cont_mais_18 += 1
    if sexo == 'M':
        cont_homens += 1
    elif sexo == 'F' and idade < 20:
        cont_mulheres_menos_20 += 1   
    mais_cadastro = input('Gostaria de cadastrar mais dados? [S/N]: ').strip().upper()
    while mais_cadastro not in 'SN':
        print('Opção inválida! Digite S para Sim e N para Não.')
        mais_cadastro = input('Gostaria de cadastrar mais dados? [S/N]: ').strip().upper()
    if mais_cadastro == 'N':
        break


print(f'O total de pessoas com mais de 18 anos é: {cont_mais_18}')
print(f'Há um total de {cont_homens} homens cadastrados')
print(f'Há {cont_mulheres_menos_20} mulheres com menos de 20 anos ')

