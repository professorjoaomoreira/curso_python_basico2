print('\033[34:51:49m{:=^90}'.format("Digitar dois numero e descobrir qual é o maior: "))
n1 = int(input('\033[m \nDigite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
        print('O n1: {}, é maior que o n2: {}'.format(n1,n2))
elif n2 > n1:
        print('O n2: {}, é maior que o n1: {}'.format(n2,n1))
else:
        print('Os números são iguais:')

print('\n\033[31:51:49m{:.^90}'.format('FINAL DO PROGRAMA'))

