'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
o mais baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte
a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
'''

# Inicializa as variáveis
codigo_mais_alto = codigo_mais_baixo = codigo_mais_gordo = codigo_mais_magro = None
mais_alto = mais_gordo = 0
mais_baixo = mais_magro = float('inf') # Inicializa com infinito para garantir que qualquer valor inserido seja menor
soma_alturas = soma_pesos = contador_clientes = 0

# Loop principal para coletar os dados dos clientes
while True:
    codigo = int(input('Digite sua matrícula (digite 0 para sair): '))
    if codigo == 0:
        break

    altura = float(input('Digite sua altura (em metros): '))
    peso = float(input('Digite seu peso (em kg): '))

    # Atualiza o cliente mais alto e mais baixo com base na altura informada
    if altura > mais_alto:
        mais_alto = altura
        codigo_mais_alto = codigo
    if altura < mais_baixo:
        mais_baixo = altura
        codigo_mais_baixo = codigo

    # Atualiza o cliente mais gordo e mais magro com base no peso informado
    if peso > mais_gordo:
        mais_gordo = peso
        codigo_mais_gordo = codigo
    if peso < mais_magro:
        mais_magro = peso
        codigo_mais_magro = codigo

    # Acumula os dados para cálculo de médias
    soma_alturas += altura
    soma_pesos += peso
    contador_clientes += 1

# Verifica se algum cliente foi registrado
if contador_clientes > 0:
    media_altura = soma_alturas / contador_clientes
    media_peso = soma_pesos / contador_clientes

    # Exibe os resultados
    print(f'\nCliente mais alto: Código {codigo_mais_alto} com {mais_alto:.2f} m')
    print(f'Cliente mais baixo: Código {codigo_mais_baixo} com {mais_baixo:.2f} m')
    print(f'Cliente mais gordo: Código {codigo_mais_gordo} com {mais_gordo:.2f} kg')
    print(f'Cliente mais magro: Código {codigo_mais_magro} com {mais_magro:.2f} kg')
    print(f'Média das alturas: {media_altura:.2f}m')
    print(f'Média dos pesos: {media_peso:.2f}kg')
else:
    print('Nenhum cliente foi registrado.')

