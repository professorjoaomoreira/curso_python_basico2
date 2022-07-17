#biblioteca Random serve para fazer um algoritmo para que o python escoha um número aleatório
from time import sleep

print('{:=^90}'.format('fazer um jogo onde penso em um numero ver se computador descobre'))
import random
from time import sleep
numero = (random.randint(1,5))
num = int(input('Escolha um número inteiro entre 1 e 5 e digite: '))
print('você: {}\ncomputador: {}' .format(num,numero))
print('PROCESSANDO...')
sleep(2)
if num == numero:
    print('Parabens!! Você venceu: O número escolhido por você foi: {} e o número escolhido pelo computador foi: {}'.format(num, numero))
else:
    print('Tente novamente! O número escolhido por você foi: {} e o computador escolheu: {}'.format(num, numero))