print('\033[1:34:51:49m{:=^90}'.format('Faça um algoritmo que leia numeros pares de 1 a 50: '))
print('\033[m')

for n in range(1,51):
    if (n % 2 == 0) :
        print('\033[1:34:49m',n,end='')
    else:
    #elif (n % 3 == 0 ):
       print('\033[1:31:49m', n, end='')
print('\n\033[1:32:49m''os numeros em azul são pares e os vermelhos são impares')


