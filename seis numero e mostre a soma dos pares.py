print('\033[1:31:51:49m{:=^90}'.format('seis numeros mostrar a soma dos nº pares:'))
print('\033[m')
soma = 0
cont = 0

for n in range(1, 7):
    num = int(input('Digite o {}º número: '.format(n)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1


    else:
        print('esse numero não é par digite um numero par')

print('Voce informoou {} números pares e a soma entre eles é de: {}'.format(cont, soma))





