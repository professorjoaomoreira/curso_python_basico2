print('{:=^90}'.format('calcular o ano bissexto com biblioteca do python'))

ano = 2024

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('É bissexto')
else:
    print('Não é bissexto')
print('{:.^90}'.format('FINAL DO PROGRAMA'))


#from calendar import isleap
from datetime import date
#ano = date.today().year
#if ano == 2017:
#if isleap(ano):