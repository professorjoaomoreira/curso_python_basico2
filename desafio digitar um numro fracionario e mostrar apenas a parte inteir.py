print('{:=^90}'.format('Arrendondando um Número no Python!'))
# fazer um algoritmo que pegue um numero fracionario e mostre apenas a parte inteira
import math
num = float(input('Digite um numero flutuante com varias casas apos o ponto. USE PONTO E NÃO VIRGULA '))
#ao digitar use . e não ,
print('\n' 'O número digitado é: {}.'
      '\n' 'O número digitado somente com a parte inteira é:{:.0f}. '
      '\n' 'O número arrendondado para baixo é:{}.'
      '\n' 'O número arrendondado para cima é:{}.'
      '\n' 'O número arrendondado pegando apenas o numero antes da virgula é: {}.'
      .format(num, num, math.floor(num), math.ceil(num), math.trunc(num)))
#===================================================================================
print('{:=^90}'.format('Final do Programa!'))