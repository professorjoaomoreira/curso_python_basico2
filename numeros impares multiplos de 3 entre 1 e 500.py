print('\033[1:34:51:49m{:=^90}'.format('algoritmos para calcular numeros impares multiplos de 3 entre 1 e 500'))
print('\033[m')
cont = 0
soma = 0
for n in range(1,501,2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
        print(n,end=' ')
print ('\n''o numero de numero entre 1 e 500 é: ',cont)
print('A soma entre os numero  multiplos de 3 é:',soma)