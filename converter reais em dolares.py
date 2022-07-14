print('{:=^50}'.format('Converter reais em dolares'))
reais = (float(input('Digite aqui o valor que você tem em reais: R$ ')))
conver = (reais / 5.26)
print ('Com seus R${}, reais, você consegue compar US${:.2f}, dolares:'.format(reais, conver))