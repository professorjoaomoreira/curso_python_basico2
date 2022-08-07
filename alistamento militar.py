print('\033[1:34:51:49m{:=^90}'.format("Calcular o ano do Alistamento Militar"))
from datetime import date
atual = date.today().year
sexo = (str(input('''\033[m

[ F ] Escolha: F - se for Femino
[ M ] Escolha: M - se for Masculino

Escolha aqui sua opção: >>  
''')))
print('sua opção foi: {}. '.format(sexo))

if sexo == ('F') or sexo == ('f'):
    print('Você é do sexo femino não precisa servir o exercito, até logo')
elif sexo == ('M') or sexo == ('m'):
    print('Você é do sexo masculino responda a próxima questão proposta')

    nasceu = int(input('Digite o ano do seu nascimento: '))
    ano = 2022
    idade = ano - nasceu
    menor = 18 - idade
    servir = ((ano + menor) - 1)
    serviu = nasceu + 18

    if idade == 18:
        print(
            'Você nasceu em: {}, tem: {} anos em {}. Você deve servir em: {}, seu alistamento foi em:{}'.format(nasceu,
                                                                                                                idade,
                                                                                                                ano,
                                                                                                                ano,
                                                                                                                ano - 1))
    elif idade < 18:
        print(
            'Você nasceu em: {}, tem: {} anos em {}. Você deve servir em: {}, seu alistamento sera em:{}'.format(nasceu,
                                                                                                                 idade,
                                                                                                                 ano,
                                                                                                                 ano + menor,
                                                                                                                 servir))
    else:
        print(
            'Você nasceu em: {}, tem: {} anos em {}. Você deve servir em: {}, seu alistamento sera em:{}'.format(nasceu,
                                                                                                                 idade,
                                                                                                                 ano,
                                                                                                                 ano + menor,
                                                                                                                 servir))

        print('Tempo que voce já saiu do exercito é de: {}'.format(atual - serviu))







else:
    print('voce não escolheu uma opão valida, tente novamente')



print('\n\033[1:31:51:49m{:.^90}'.format('FINAL DO PROGRAMA'))