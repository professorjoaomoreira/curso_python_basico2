print('{:=^90}'.format('este algoritmos é para calcular 5% de desconto em um produto'))
produto = float(input('Qual o valor do produto: '))
desconto = ((5 * produto)/100)
print('O valor do produto que você deseja é de: R${:.2f}, mas com 5% de desconto fica por R${:.2f} reais.'.format(produto, (produto - desconto)))

print('{:=^90}'.format('final do programa'))
