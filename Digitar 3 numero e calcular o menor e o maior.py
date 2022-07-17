print('{:=^90}'.format('Criar um algoritmo que leia 3 numeros e imprima o maior e o menor'))
n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
n3 = float(input('digite o terceiro número: '))

if (n1 > n2 ) and (n1 > n3):
    print('n1 é o maior número: ')
if (n2 > n1) and (n2 > n3):
    print('n2 é o maior número: ')
if (n3 > n2) and (n3 > n1):
    print('n3 é o maior número: ')

if (n1 < n2 ) and (n1 < n3):
    print('n1 é o menor número: ')
if (n2 < n1) and (n2 < n3):
    print('n2 é o menor número: ')
if (n3 < n2) and (n3 < n1):
    print('n3 é o menor número: ')


