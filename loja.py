print('----Loja de eletronicos----\n')

produtos = {'ipad': 4000,'iphone': 3500,'macbook':8000,'fone': 800, 'relogio': 1500}
print(produtos)

escolha = input('Qual produto você deseja: ').lower().strip()

if escolha in produtos:
    quantas = int(input(f'Quantos {escolha} você quer: '))
    preço = produtos[escolha]
    total = preço * quantas
    if total > 6000:
        desconto = 0.20
        totalf = total * (1 - desconto)
    else:
       totalf = total

print(f'O total da compra deu: R${totalf}')

escolha2 = input('Deseja comprar mais algo?(Sim = 1)(Não = 0): ').lower().strip()

if escolha2 == '1':
    prdto = input('Qual produto você quer: ')
    if prdto in produtos:
        quantas2 = int(input(f'Quantos {prdto} você quer: '))
        preço2 = produtos[prdto]
        print(f'O seu {prdto}, custa R${preço2}')
        totalr = totalf + preço2 * quantas2
        print(f'Seu novo total é {totalr} ')
        print('=== RESUMO ===\n')
        print(f'{escolha} x{quantas} = R${preço}')
        print(f'{escolha2} x{quantas2} = R${preço2}')
        print(f'O total geral: R${totalr}')
 
    else:
        print('Produto inexistente')
else:
    print('Até mais,aqui está seu resumo\n')
    print('=== RESUMO ===')
    print(f'{escolha} x{quantas} = R${preço}')
    print(f'O total é: {totalf}')