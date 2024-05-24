# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


letra = input('Digite qualquer letra: ').lower().strip()

lista_vogal = ['a', 'e', 'i', 'o', 'u']

if len(letra) == 1 and letra.isalpha(): # isalpha verifica se a entrada é uma letra do alfabeto.
    if letra in lista_vogal:
        print('Sua letra é uma vogal!')
    else:
        print('Sua letra é uma consoante!')
else:
    print('Entrada inválida! Digite uma única uma letra.')            