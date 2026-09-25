lista = []

def adiconar_item(lista):
    itens = input('Qual item você quer adicionar? ')
    lista.append(itens)


def mostra(lista):
    for itens in lista:
        print(itens)

while True:
    print('1 - Adicionar')
    print('2 - Mostrar')
    print('3 - Sair')

    opção = int(input('Digite sua escolha: '))

    if opção == '1':
        adiconar_item(lista)
    elif opção == '2':
        mostra(lista)
    elif opção == '3':
        break
    else:
        print('Opção invalida')












































