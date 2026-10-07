def definido():
    senha = input('Digite sua senha: ')
    numeros = '0123456789'

    tem_numero = any(numero in senha for numero in numeros)

    if len(senha) >= 15 and tem_numero:
        print('Sua senha é forte porque tem 15+ caracteres e números')
    elif 10 <= len(senha) < 15 and tem_numero:
        print('Sua senha é média')
    elif len(senha) < 10:
        print('Sua senha é mais ou menos')
    else:
        print('Sua senha é fraca')


def indefinido():
    senha = input('Digite sua senha: ')
    carac = int(input('Quantos caracteres sua senha deve ter: '))
    numeros = input('Sua senha deve conter números: ').capitalize().strip()

    tem_numero = any(numero in senha for numero in '0123456789')

    if numeros == 'Sim':
        if len(senha) >= carac and tem_numero:
            print('Sua senha é forte')
        else:
            print('Sua senha é fraca')
    else:
        if len(senha) >= carac:
            print('Senha forte')
        else:
            print('Senha fraca')


while True:
    print('== Verificador Senha ==')
    print('1 = Definido')
    print('2 = Valores do Definido')
    print('3 = Você define')
    print('4 = Sair')

    opção = int(input('Opção: '))

    if opção == 1:
        definido()

    elif opção == 2:
        print('Caso sua senha tenha 15 ou mais caracteres e tenha números, ela é forte.')
        print('Caso tenha entre 10 e 14 caracteres e números, ela é média.')
        print('Caso tenha menos de 10 caracteres, ela é mais ou menos.')
        print('Caso não siga esses critérios, ela é fraca.')

    elif opção == 3:
        indefinido()

    elif opção == 4:
        break

    else:
        print('Opção inexistente')

