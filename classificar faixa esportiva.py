from datetime import date
atual = date.today().year
print('\033[1:34:51:49m{:=^90}'.format('Faixas de Classificação Desportiva'))
nasc = int(input('\033[mDigite a Data de Nascimento do Atleta: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <=14:
    print('classificação: infantil')
elif idade <= 19:
    print('classificação junior')
elif idade <= 25:
    print('classificação senior')
else:
    print('classificação: master')
print('\033[1:31:51:49m{:.^90}'.format('FINAL DO PROGRAMA'))