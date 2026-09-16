#Formatação  numerica
faturamento = 1000000 #se eu por'_' para entender melhor qual numero é nao afeta no codigo
custo = 270

lucro = int(faturamento - custo)
margem = lucro / faturamento
texto = f'O lucro foi de R${lucro: ,.2f} e o faturamento foi de R${faturamento:,.2f} e a margem foi de: {margem:.1%}'

print(texto)

email = 'EMAIL_FALSO@gmail.com '

email = email.lower() #colocar letra minuscula
email = email.strip() #ajustar espaços

print(email)

#tamanho
print(len(email)) #CONTAR CARACTERES
#posição
posição = email.find('@gmail.com')#ACHAR
print(posição)

#PEDAÇOS DO TEXTO
print(email[11:])
servidor = email[posição+1:]
print(servidor)

email = 'FELIPEX@gmail.com'
#TROCAR UM PEDAÇO DO TEXTO

novo_email = email.replace("gmail.com" , "yahoo.com.br")
print(novo_email)

nome = 'joão lira'
nome = nome.title()
print(nome)
nome = nome.capitalize()
print(nome)
nome = nome.upper()
print(nome)


# exercicios


nome = 'Felipe Jesus de Sousa'
email = 'emailfalsodofelipe@gmail.com'

#descubra o servidor do email
posição = email.find('@')
print(posição)
servidor = email[posição:]
print(servidor)
#descubra o 1 nome de usuario
posição = nome.find(' ')
print(posição)
primeiro_nome = nome[:posição]
print(primeiro_nome)
#criar um mensagem personalizada dizendo 'Usuario 1 nome foi cadastrado com sucesso no email tal'

mensagem = f'Usuario {primeiro_nome} foi cadastrado com sucesso no email {email}'
print(mensagem)




































# print('Banco de Teste')
# print('By felipe')

# nome = str(input('Digite o seu nome inteiro: '))  
# print(nome)
   
# email= str(input('Digite o seu email inteiro: '))

# print(email)

# cpf = str(input('Digite seu CPF: '))

# if len(cpf) != 11:
#     print('CPF inválido')

# else:
#     print('CPF cadastrado com sucesso!')

# numero_telefone = float(input('Digite o numero do seu telefone(COM O DDD): '))

# mensagem1 = 'O seu numero de telefone foi cadastrado com sucesso!'

# if numero_telefone > 9999999999999:
#     print('Numero inválido')

# else:
#     print(mensagem1)

# saldo = float(input('Digite seu saldo: '))

# sim = 1
# não = 2

# if saldo <= 1000:
#     print('Você está quebrado!!')
#     emprego = int(input('Deseja um emprego? Sim = 1 Não = 2 '))

#     if emprego  == 1 : 
#         print('Você está contratatdo')
    
#     elif emprego == 2:
#          print('Você está fardado ao fracasso!')
    
#     else:
#         print('Opção inválida')
    
# elif saldo >= 10000:
#     print('Você está estavel!')
   


# investimentos = float(input('Digite o dinheiro que você tem investido: '))
# print(f'O seu total em investimentos é: {investimentos}')

# if investimentos < 100:
#     print('Você precisa investir mais!!')
#     investir_melhor = int(input('Você quer aprender a investir? (sim = 1 não = 2): '))

#     if investir_melhor == 1:
#         print(f'O usuario chamado {nome} acabou de receber aulas de como investir no seu email que é {email}')

#     elif investir_melhor == 2:
#         print('Vai acabar endividado!')

#     else:
#         print('Opção inválida')


# devendo = float(input('Qunto dinheiro você está devendo: '))
# print(f'Suas dividas já somam: {devendo}')

# if devendo > 1000:
#     print('Você precisa quitar suas dividas!')
#     dever_menos = int(input('Quer quitar suas dividas? (Sim = 1 , Não = 2) '))

#     if dever_menos == 1:
#         print(f'O usuario chamado {nome} recebeu uma mensagem no email onde ele recebera instruções para quitar sua dividas!!')

#     elif dever_menos == 2:
#         print('CUIDADO!! suas dividas são uma bola de neve')

#     else:
#         print('Opção invalida')




