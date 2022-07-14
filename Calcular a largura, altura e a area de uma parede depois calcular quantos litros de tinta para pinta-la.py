print('{:=^70}'.format('Calcular a area de uma parede'))
comprimento = float(input('Digite o comprimento da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = largura * comprimento
pintar = area / 2
print ('A area da parede informada por você é de {}, m², então precisa de {} litros de tinta para pinta-la'.format(area, pintar))


print('{:=^70}'.format('Final do programa'))