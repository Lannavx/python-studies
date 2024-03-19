#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz_quadrada = n1 **(1/2)
print(f' O dobro do número {n1} é {dobro}. \n E seu triplo é {triplo} \n Já a sua raiz quadrada é {raiz_quadrada:.2f}')

#Outra forma de fazer

n1 = int(input('Digite um número: '))
print(f' O dobro do número {n1} é {(n1*2)}. \n E seu triplo é {(n1*3)} \n Já a sua raiz quadrada é {(n1**(1/2)):.2f}')