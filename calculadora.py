print('Calculadora Do Felipex')
print(' 1 = soma')
print(' 2 = subtração')
print(' 3 = divisão')
print(' 4 = Mutiplicação')

operação = input('Qual operação você quer fazer? ')

numero_1 = float(input('Digite o primeiro numero: '))
numero_2 = float(input('Digite o segundo numero: '))

if operação == '1':
	resultado = numero_1 + numero_2
	print(f'O resultado da soma é: {resultado}')

elif operação == '2':
	resultado = numero_1 - numero_2
	print(f'O resulrado da subtraação é: {resultado}')

elif operação == '3':
	resultado = numero_1 * numero_2
	print(f'O resultado da divisão é: {resultado}')

elif operação == '4':
	resultado = numero_1 / numero_2
	print(f'O resultado da mutiplicação é: {resultado}')

elif operação > '4':
	print('Operação inexistente')


