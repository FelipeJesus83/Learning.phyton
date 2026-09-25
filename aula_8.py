
# # Bonus 1: de 2 reais por venda feita
# # bonus 2: 1% do valor das vendas
# def calcular_bonus(vendas):
#     bonus1 = 2 * len(vendas)
#     bonus2 = 0.01 * sum(vendas)

#     return bonus1, bonus2


# # vendas = [100,200,250,1000]
# # Unpacking da tupla 
# bonus1, bonus2 = calcular_bonus(vendas) 
# #So da certo se tiveer a mesma quantidade de valores do return,o nome pode ser quaquer um
# # no terminal vem em formatos de tuplas

# print(bonus1)
# print(bonus2)

# telas = [(1080, 1030), (1090, 1320)]
# for altura, largura in telas:
#     print(f'A altura é: {altura} e a largura é:  {largura}')


#Exercicio

# Bonus 1: de 2 reais por venda feita
# bonus 2: 1% do valor das vendas
def calcular_bonus(vendas):
    bonus1 = 2 * len(vendas)
    bonus2 = 0.01 * sum(vendas)

    return bonus1, bonus2

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

# bonus de cada funcionario
# total de bonus 1 pago aos funcionários
# total de bonus 2 pago aos funcionários
total_bonus1 = 0
total_bonus2 = 0
for funcionario in vendas:
    b1, b2 = calcular_bonus(vendas[funcionario])
    print(f'O  bonus 1 do {funcionario} é: {b1}')
    print(f'o bonus 2 do {funcionario} é: {b2}')
    total_bonus1 = total_bonus1 + b1
    total_bonus2 = total_bonus2 + b2
    print(f'O total de Bonus 1 é de: {total_bonus1}')
    print(f'O total de Bonus 2 é de: {total_bonus2}')
    print(f'O total geral de Bonus é de: {total_bonus1 + total_bonus2}')




























