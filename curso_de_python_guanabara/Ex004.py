#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite um valor: ')

print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?' , n.isnumeric())
print('É alfabetico?' ,  n.isalpha())
print('É alfanúmerico?' , n.isalnum())
print('Está em maiusculas?' ,  n.isupper())
print('Está em minusculas?' , n.islower())