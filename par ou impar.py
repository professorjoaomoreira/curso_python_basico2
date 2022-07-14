print('{:=^90}'.format('Algoritmos para calcular se um número é par ou impar'))
num = int(input('Digite um número: '))
par = num % 2 == 0

if num % 2 == 0:
    print('O número ínformado é: {} e é: par'.format(num))
else:
    print('O número informado é: {} e é: impar'.format(num))