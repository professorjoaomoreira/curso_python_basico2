from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1,5):
    nasc = int(input('em que ano a {}ª pessoa nasceu: '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior =+ 1

    else:
        totmenor =+ 1

print('Total de {} pessoas de maior: '.format(totmaior))
print('Total de {} pessoas de menores: '.format(totmenor))



