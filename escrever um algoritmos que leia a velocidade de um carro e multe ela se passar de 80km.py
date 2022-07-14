print('{:=^90}'.format('algoritmo para calcular a velocidade do carro e multar se necessario'))
vel = float(input('Digite a velocidade do seu carro!! '))
print ('A velocidade informada foi: {:.0f} km/h'.format(vel))
exc = vel - 80
multa = exc * 7

if vel > 80:
    print('Você esta a: {:.0f} km/hora esta: {:.0f}km/h acima da velocidade permitida, sua multa é de: R${:.2f}'.format(vel, exc, multa))
else:
    print('Parabens!! sua velocidade é: {:.0f}. Você é um cidadão conciente esta dentro dos limetes de velocidade'.format(vel))