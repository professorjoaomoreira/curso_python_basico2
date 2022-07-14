print('{:=^90}'.format('digitar um nome e ver se tem silva na digitação'))
nome = (input(('digitar um nome: ').strip()))
print('O texto digitado tem silva? {}'.format('SILVA' in nome.upper()))
print(' O texto digitado tem silva? {}'.format('silva' in nome.lower()))
