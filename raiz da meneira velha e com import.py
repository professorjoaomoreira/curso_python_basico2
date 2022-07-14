# import math = importa toda a biblioteca math
#from math import sqrt = este formato importa apenas um serviço especifico da biblioteca
from math import sqrt

num = int(input('Digite o valor para calcular a raiz quadrada: '))
raiz_velha = (num**(1/2))
raiz_nova = (sqrt(num)) #no caso de usar o from ai tem que remover o math desta linha
print('A raiz quadrada usando biblioteca do python é: {} é: {}'.format(num, raiz_nova))
print('A raiz quadrada usando a técnica antiga de {} é: {}'.format(num, raiz_velha))