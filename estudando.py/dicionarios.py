lista_produtos = ['ipad', 'iphone', 'mac book']
lista_preços =[7000, 5000, 2000]

dic_produtos = {'ipad': 7000, 'iphone': 5000, 'macbook':2000}

# lista_produtos.append('pamonha')

#pegar um item
# produto = 'iphone'
# posição = lista_produtos.index(produto)
# preço = lista_preços[posição]
# print(produto, preço)


# dic_produtos['iphone']
print(dic_produtos['iphone'])

dic_vendas = {'lira':[1000, 500, ], 'joão':[2000, 1000, 500]}
print(dic_vendas['lira'])


#adcicionar um item
dic_produtos['macbook'] = 1200
#editar um item
dic_produtos['iphone'] = 500
print(dic_produtos)

print(dic_produtos)
#remover
item_removido = dic_produtos.pop('macbook')
print(dic_produtos)
print(item_removido)
#verificar se exite um item

print('iphone' in dic_produtos)
print('iphone' in dic_produtos.keys())
print(7000 in dic_produtos.values())

produto = list(dic_produtos.keys())
print(produto)

preços = list(dic_produtos.values())
print(preços)

soma_preços = sum(dic_produtos.values())
print(soma_preços)


