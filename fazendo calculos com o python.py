#desenvolvendo calculos com (),**,*,//,/,+,- e %.
n1 = int(input('Digite o n1: '))
n2 = int(input('Digite o n2: '))
paren1 = (n1 * n2)-n1
exp2 = n1 ** n2
mult3 = n1*n2
div4 = n1 / n2
divdir5 = n1 // n2
soma6 = n1 + n2
subtra7 = n1 - n2
resto8 = n1 % n2
print('O resultado da resolução dos parentes é: ',paren1,end ='')
print(' , O resultado da potencia é: ',exp2)
print(' e O resultado da multiplicação é:{:.5f}  '.format (mult3),end ='')
print('O resultado da divisão é: ',div4,end='')
print(' e o resultado da divisão inteira é: ',divdir5)
print('O resultado da soma é: ',soma6,end='')
print(', o resultado da subtração é ',subtra7)
print('O resultado do resto da divisão é: ',resto8)

#para dividir um print usar \n
#para unir dois prints usa \,end =''
