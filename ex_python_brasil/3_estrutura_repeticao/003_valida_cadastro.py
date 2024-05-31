'''
Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd'
'''

# Entrada e validação do nome, requer mínimo de 3 caracteres.
nome = input('Informe seu nome: ').strip()
while len(nome) < 3:
    print('Nome inválido! Por favor, escreva um nome com mais de 3 caracteres.')
    nome = input('Informe seu nome: ').strip() 

# Entrada e validação da idade, aceitável entre 0 e 150 anos.
idade = int(input('Informe sua idade: '))
while idade < 0 or idade > 150:
    print('Idade inválida! Por favor, informe uma idade entre 0 e 150.')
    idade = int(input('Informe sua idade: '))

# Entrada e validação do salário, deve ser maior que zero.
salario = float(input('Informe sua renda mensal: R$'))
while salario < 0:
    print('Salário inválido! Por favor, insira um valor maior que zero para o salário.')
    salario = float(input('Informe sua renda mensal: R$'))

# Entrada e validação do sexo, deve ser 'F' (Feminino) ou 'M' (Masculino).
sexo = input('Informe F para feminino ou M para masculino: ').strip().upper()  
while sexo not in ['F', 'M']:
    print('Sexo inválido! Por favor, informe os dados corretos.')    
    sexo = input('Informe F para feminino ou M para masculino: ').strip().upper()

# Entrada e validação do estado civil, deve ser 'S', 'C', 'V', ou 'D'.
estado_civil = input('Informe seu estado civil: [S] solteiro, [C] casado, [V] viuvo ou [D] divorciado: ').strip().upper()
while estado_civil not in ['S', 'C', 'V', 'D']:
    print('Estado Civil incorreto! Por favor, informe seu estado civil corretamente.')    
    estado_civil = input('Informe seu estado civil: [S] solteiro, [C] casado, [V] viuvo ou [D] divorciado: ').strip().upper()

# Conversão de códigos de sexo e estado civil para descrições completas.
sexo = {'F': 'Feminino', 'M': 'Masculino'}.get(sexo, sexo)
estado_civil = {'S': 'Solteiro', 'C': 'Casado', 'V': 'Viuvo', 'D': 'Divorciado'}.get(estado_civil, estado_civil)
            
print(f''' 
Nome: {nome}
Idade: {idade}
Salário: R${salario:.2f}
Sexo: {sexo}
Estado Civil: {estado_civil}
''')   