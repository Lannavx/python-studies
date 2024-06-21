'''Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série'''

# Loop infinito que continuará executando até que seja explicitamente interrompido
while True:

  # Solicita ao usuário um número para determinar o número de termos da série
  termo = int(input('Informe um número inteiro e postivo (informe zero para sair): '))

  # Condição de parada do loop
  if termo == 0:
    break

  # Inicializa as variáveis
  numerador = 1
  denominador = 1
  soma = 0

  # Inicia uma lista vazia para armazenar os termos como strings
  termos_str = []

  # Loop para calcular cada termo da série até atingir n termos
  while numerador <= termo:

    # Calcula o termo atual e adiciona à soma
    termo_atual = numerador / denominador
    soma += termo_atual

    # Adiciona cada termo formatado como string à lista
    termos_str.append(f'{numerador}/{denominador}')
    
    # Incrementa o numerador e o denominador para o próximo termo
    numerador += 1
    denominador += 2

  # Junta todos os termos com ' + ' entre eles
  serie_str = " + ".join(termos_str)

  # Imprime a série completa com o resultado
  print(f'S = {serie_str} = {soma:.2f}')