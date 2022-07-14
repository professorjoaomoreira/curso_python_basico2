nome = input('Qual o seu nome ')
msg = ('prazer em te conhecer {:20}! \n'.format(nome)) #espaços invisiveis
msg1 = ('prazer em te conhecer {:>20}!\n'.format(nome))#espaços com recuo a direita
msg2 = ('prazer em te conhecer {:<20}!\n'.format(nome))#espaço com recuo a esquerda
msg3 = ('prazer em te conhecer {:^20}!\n'.format(nome))#espaços centralizados
msg4 = ('prazer em te conhecer {:=^20}!\n'.format(nome))#espaços cetralizados e com =
print (msg,msg1,msg2, msg3,msg4)

