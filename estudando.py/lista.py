# lista_vendas = [500, 100 , 570]

# print(lista_vendas[0])

# #tamanho da lista
# tamanho_lista = len(lista_vendas)

# #operações coma lista
# total_vendas = sum(lista_vendas)

# print(sum(lista_vendas))

# #max min e media
# print(max(lista_vendas))
# print(min(lista_vendas))
# print(total_vendas / tamanho_lista)

#encontra um elemento em uma lista (posição do elemento da lista)

# lista_produtos = ['pao' , 'torrada']
# print('pao' in lista_produtos)

# posição = lista_produtos.index('pao')
# print(posição)

# pedaço_lista = lista_produtos[posição:]
# print(pedaço_lista)

# #editar um item dentro da lista

# lista_preço = [50, 20]

# nov_preço = int(lista_preço[0] * 1.1)

# lista_preço[0] = nov_preço

# print ((lista_preço))

# #remover item da lista
# # lista_produtos.remove('pao')
# # print(lista_produtos)

# # lista_produtos.pop(0)
# # print(lista_produtos)

# #adicionar

# lista_produtos.append('pao')
# print(lista_produtos)

# lista2 = ['bolacha' , 'bolo' , 'biscoito']
# lista_produtos.extend(lista2)
# print(lista_produtos)

# #inserir um item em uma posição especifica

# lista_produtos.insert(0,'mouse gamer')
# print(lista_produtos)

# #contar qntas vezes um item aparece na lista
# print(lista_produtos.count('pao'))

# #ordenar uma lista
# #em ordem alfabetica de acordo com a ASCII
# lista_produtos.sort()
# print(lista_produtos)

# #decresente
# lista_preço.sort(reverse=True)
# print(lista_preço)

# #creseecnete
# lista_preço.sort(reverse=False)
# print(lista_preço)






#RESUMO

# Função	O que faz	Como usa

# len()	Conta	len(lista)

# sum()	Soma	sum(lista)

# append()	Adiciona	lista.append(coisa)

# index()	Acha posição	lista.index(coisa)

# strip()	Tira espaços	texto.strip()

# lower()	Letra pequena	texto.lower()

# upper()	Letra grande	texto.upper()

# title()	1ª Grande Cada Palavra	texto.title()

# capitalize()	1ª Grande, Resto Pequeno	texto.capitalize()

# replace()	Troca texto	texto.replace('antes', 'depois')

# find()	Acha posição de texto	texto.find('coisa')

# in	Verifica se existe	coisa in lista

# {:,}	Formata com vírgula	f'{numero:,}'




lista_nome = []

nome1 = input('Digite o primeiro nome: ').lower()
lista_nome.append(nome1)
nome2 = input('Digite o segundo nome: ').lower()
lista_nome.append(nome2)
nome3 = input('Digite o terceiro nome: ').lower()
lista_nome.append(nome3)

print(f'O total de nomes foi: {len(lista_nome)}')
print(lista_nome)

