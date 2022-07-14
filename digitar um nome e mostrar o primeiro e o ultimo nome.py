print('{:=^90}'.format('Digitar um nome e mostrar o primeiro nome e o ultimo sobrenome: '))
n = str(input('Digite seu nome completo: ').strip())
nome = n.split()
print('o nome digitado é: {}'.format(n))
print('o primeiro nome é: {}'.format(nome[0]))
print('o ultimo nome é: {}'.format(nome[len(nome)-1]))

print('{:.^90}'.format('FINAL DO PROGRAMA'))