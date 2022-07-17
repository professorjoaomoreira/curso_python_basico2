print('{:=^90}'.format('Algoritmo para calcular o valor da passagem'))
dist = float(input('Informe quantos quilometros vai fazer nesta viagem? '))
menos = dist * 0.50
mais = dist * 0.45
if dist >= 200:
    print('A sua passagem vai custar: R${:.2f}'.format(dist * 0.50))
else:
    print('A sua passagem vai custar: R${:.2f}'.format(dist * 0.45))

