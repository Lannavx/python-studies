'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
 igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

nome_usuario = input('Informe o nome de usuário: ')
senha = input('Senha: ')

# Continua solicitando uma nova senha enquanto ela for igual ao nome de usuário
while senha == nome_usuario:
    print('Senha não pode ser igual ao nome de usuário. Por favor, informe uma nova senha.')
    senha = input('Senha: ')

print('Nome de usuário e senha registrados com sucesso!')