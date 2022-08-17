import time
import random
#from random import randint
#from time import sleep
print('\033[1:34:51:49m{:=^90}'.format('Fazer um Game para jogar jokenpo'))

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint (0,2)
print('\033[m')

jogador = (int(input('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura
Qual é a sua jogada? \n''')))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

print('-=' * 15)
print('O jogador jogou: \033[1:39:43:39m{}\033[m \nO computador jogou:\033[1:30:42:39m{}\033[m'.format(itens[jogador], itens[computador]))
print('-=' * 15)

if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('jogador venceu!!!')
    elif jogador == 2:
        print('computador venceu!!!')
    else:
        print('valor invalido tente novamente')

elif computador == 1:
    if jogador == 1:
        print('EMPATOU')
    elif jogador == 0:
        print('computador venceu!!!')
    elif jogador == 2:
        print('jogador venceu!!!')
    else:
        print('valor invalido tente novamente')

elif computador == 2:
    if jogador == 2:
        print('EMPATOU')
    elif jogador == 1:
        print('computador venceu!!!')
    elif jogador == 0:
        print('jogador venceu!!!')
    else:
        print('valor invalido tente novamente')

print('\033[1:31:51:49m{:=^90}'.format('FINAL DO PROGRAMA'))










