soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont +1
        soma = soma + c

        #print(c, end=' ')
        print('A soma de todos é: {}'.format(soma))
        print('A contagem dos valores é: {}'.format(cont))