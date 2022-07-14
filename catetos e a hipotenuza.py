print('{:=^90}'.format('algoritmos para calcular os catetos e a hipotenuza'))
ca = float(input('informe o valor do cateto adjacente: '))
co = float(input('informe o valor do cateto oposto: '))
hi = int((ca**2 + co**2)**(1/2))
print('O valor da hipotenuza é: {}'.format(hi))

print ('{:=^90}'.format("agora vamos fazer importando da biblioteca math"))
import math
ca = float(input('informe o valor do cateto adjacente: '))
co = float(input('informe o valor do cateto oposto: '))
hi = (math.hypot(ca, co))
print('O valor da hipotenusa é {:.0f}'.format(hi))