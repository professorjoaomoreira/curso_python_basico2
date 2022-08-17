from datetime import date
totmaior = 0
totmenor = 0
soma = 0
atual = date.today().year

for pessoa in range(1,3):
    ano = int(input('digite o ano que a {}ª pessoa nasceu: '.format(pessoa)))
    idade = atual - ano

    if idade >= 18:
        totmaior += 1


    else:
        totmenor += 1

print(totmaior)
print(totmenor)







