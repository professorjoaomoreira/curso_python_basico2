print('{:=^90}'.format("conversao de grau celsium para faranheit"))
cel = float(input("Digite a temperatura em graus celsius: "))
conversao = ((cel * 9/5) + 32)
print('A temperatura esta em {} graus celsius a conversão fica em {} graus faranhait '.format(cel, conversao))