texto = str(input('Digite um texto: ')).strip().upper()
palavra = texto.split()
junto = ''.join(palavra)
inverte = ''
for letra in range(len(junto) - 1, -1, -1):
    inverte += junto[letra]
    print(junto, inverte)
if inverte == junto:
    print('temos palindromo')
else:
    print('a frase digitada não forma palindromo')

