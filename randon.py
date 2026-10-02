import random
print('==== Sistema de Acerto de numero ====')
ate = int(input('Até que numero vocè quer sortear: '))

numero = random.randint(1, ate)
tentativas = 0
acertou = False
while not acertou:
    numero_adv = int(input('Digite um numero de 1 a 100: '))
    tentativas += 1
    if numero == numero_adv:
        acertou = True
        print(f'Você acertou em {tentativas} tentativas!')
    elif numero > numero_adv:
        print('Escolha um numero maior')
    else:
        print('Escolha um numero menor')