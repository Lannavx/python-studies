'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural, a colocação do "e", da vírgula entre outros. 
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades 
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

numero = int(input("Digite um número inteiro menor que 1000: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
saida = ""

if numero < 1000:
    if centena > 0:
        if centena == 1:
            saida += "1 centena"
        else:
            saida += f"{centena} centenas"
            
        # Adiciona a vírgula se houver dezenas ou unidades    
        if dezena > 0 or unidade > 0:
            saida += ", "

    if dezena > 0:
        if dezena == 1:
            saida += "1 dezena"
        else:
            saida += f"{dezena} dezenas"

        # Adiciona o "e" se houver unidades    
        if unidade > 0:
            saida += " e "

    if unidade > 0:
        if unidade == 1:
            saida += "1 unidade"
        else:
            saida += f"{unidade} unidades"
    
    print(f"{numero} = {saida}")
else:
    print('Número fora do intervalo permitido.')

