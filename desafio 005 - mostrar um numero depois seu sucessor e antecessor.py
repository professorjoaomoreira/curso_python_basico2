numero = int(input('digite um número: '))
ant = (numero - 1)
suc = (numero +1)
print (' O número digitado é: {} o número antecessor é: {} e o número posterior é: {}'.format(numero, ant, suc))

#outra maneira de fazer a mesma coisa com uma unica varial é

n = int(input('digite um número: '))
print('Analisando o numero: {}, vejo que seu antecessor é: {} e o seu sucessor é: {}'.format(n, n-1, n+1))