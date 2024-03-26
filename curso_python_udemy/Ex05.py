'''
Ex 1: Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.s
'''

numero = input('Digite un número: ') 

if numero.isdigit(): 
     numero_int = int(numero) 
     par_impar = numero_int % 2 == 0 
     par_impar_texto = 'ímpar' 

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {numero_int} é {par_impar_texto}')
else:
     print('Você não digitou um número inteiro')

# Outra forma 
      
numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')              
except ValueError: 
    print('Isso não é um número inteiro')


# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

''' O ValueError é um tipo de exceção no Python e é lançado quando uma operação
ou função recebe um argumento com tipo correto, mas com valor inapropriado
Por exemplo, a função int() espera um valor que possa ser convertido para inteiro. 
Se receber uma string que não representa um número inteiro (como letras ou números fracionários), 
não poderá realizar a conversão e lançará um ValueError. '''


'''
Ex 2: Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

hora = input('Informe a hora em números inteiros entre 0 e 23: ')

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora!')    
except ValueError:
    print('Por favor, digite apenas números inteiros!')


'''
Ex 3: Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
'''

nome = input('Informe seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto!')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal!')     
    else:
        print('Seu nome é muito grande!')    
else:
    print('Digite mais de uma letra!')        