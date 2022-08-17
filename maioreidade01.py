from datetime import date
print('\033[1:34:51:49m{:=^90}'.format('criar um algoritmo que leia o ano de nascimento de sete pessoas, mostre quantas são menores e quantas são maiores'))
print('\033[m'.format('limpa'))
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,3):
    ano_nasc = int(input('Digite o ano de nascimento da {}ª, pessoa: '.format(pessoa)))
    idade = atual - ano_nasc
    if idade >= 21:
        print('Essa pessoa tem {} anos. E é de maior'.format(idade))
        totmaior = totmaior + 1

    else:
        print('Essa pessoa tem {} anos. E é de menor'.format(idade))
        totmenor = totmenor + 1

    print ('Ao todo tivemos {}, pessoas maiores de idade'.format(totmaior))
    print('Ao total tivemos {}, pessoas menores de idade'.format(totmenor))

print('\033[1:31:51:49m{:.^90}'.format('FINAL DO PROGRAMA'))
