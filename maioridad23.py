import datetime
atual = datetime.date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1,3):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = atual - ano
    if idade >= 18:
        totmaior = totmaior + 1

    else:

        totmenor = totmenor + 1

print('O total de pessoas maior de idade é {} \ne o total de pessoa menores de idade é {}'.format(totmaior, totmenor))
