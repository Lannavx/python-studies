'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''


idade_soma = 0
mulher_menos_20 = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
for pessoa in range (1,5): 
   print(f'{pessoa}ª PESSOA')
   nome = str(input('Nome: ')).strip()
   idade = int(input('Idade: '))       
   sexo = str(input('Sexo [F/M]: ')).upper().strip()

   idade_soma += idade
                                        
   if sexo == 'M'and idade > idade_homem_mais_velho:
      idade_homem_mais_velho = idade
      nome_homem_mais_velho = nome

   if sexo == 'F' and idade < 20: 
      mulher_menos_20 += 1
  
media = idade_soma / 4

print(f'A média das idades informadas é de {media}')
print(f'O nome do homem mais velho é {nome_homem_mais_velho} e ele tem {idade_homem_mais_velho} anos')
print(f'Há {mulher_menos_20} mulher com menos de 20 anos')




