print('\033[1:34:51:49m{:=^90}'.format('Calcular o IMC de uma pessoa'))
peso = float(input('\033[mDigite o seu peso: '))
altura = float(input('Digite sua Altura: '))
imc = peso / (altura * altura)
print('seu IMC é de: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30:
    print('sobre peso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

print('\033[1:31:51:49m{:.^90}'.format('FINAL DO PROGRAMA'))
