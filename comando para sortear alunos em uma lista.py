import random
print('{:=^90}'.format('Algoritmo que cria uma lista e e sortea um aluno entre varios'))
alun = input('Digite o no me do aluno: ')
alun1 = input('Digite o nome do aluno: ')
alun2 = input('Digite o nome do aluno: ')
alun3 = input('Digite o nome do aluno: ')
alun4 = input('Digite o nome do aluno: ')
lista = [alun, alun1, alun2, alun3, alun4]
escolhido = random.choice(lista)
print('O aluno sorteado foi {}'.format(escolhido) )
print('{:.^90}'.format('final do programa'))