print('{:=^90}'.format('Algoritmos que calcule o valor a pagar pelo aluguel do carro'))
km = float(input('informe quantos quilometros rodados: '))
dias = int(input('informe o número de dias usando o carro: '))
cdias = (dias * 60)
ckm = (km * 0.15)
print('O carro foi alugado por {} dias. O valor a ser pago pelos dias de uso é: R${}.'
      '\n mais o valor de R${}. Pago pelos quilometros rodados.'
      '\n O valor total a ser pago é de R${}'
      .format(dias, cdias, ckm, (cdias + ckm)))