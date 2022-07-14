import random
print('{:=^100}'.format('Algoritmos para fazer uma lista sortear aleatoriamente e montar uma lista de apresentação'))
alu1 = input('Digite o nome do aluno: ')
alu2 = input('Digite o nome do aluno: ')
alu3 = input('Digite o nome do aluno: ')
alu4 = input('Digite o nome do aluno: ')
lista = [alu1, alu2, alu3, alu4]
escolhido = (random.shuffle(lista))
print('A ordem de apresentação dos trabalhos sera: {}'.format(lista))