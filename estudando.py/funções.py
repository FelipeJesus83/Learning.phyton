lista_preços = [1500, 1000, 800, 2000]

def calcular_imposto(lista_preços):
    imposto_total = 0
    for preço in lista_preços:
        if preço < 1000:
            taxa = 0.1
        else:
            taxa = 0.15
        imposto = preço * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

print(calcular_imposto(lista_preços))

list_preços = [500,200,350,470,650]

print(calcular_imposto(list_preços))


def se_increve():# FUNÇÃO QUE EXECUTA UMA AGO E N TE TRAZ ND EM RPSOTA E POR ISSO N PRECISA DO RETURN
    print('Clica no botão abaixo no video')
    print('Da um LIKE')

se_increve()


lista_preços = [1500, 1000, 800, 2000]

def maior_1000(lista_preços):
    for preço in lista_preços:
        if preço > 1000:
            print('O preço e maior que mil')
        elif preço == 1000:
            print('O preço e iguaal a 1000')
        else:
            print('O preço não é maior que mil')

maior_1000(lista_preços)

maior_1000(list_preços) # usar a função em outra lista


#usar uma função em outra

def definir_taxa(preço):
    if preço < 1000:
         taxa = 0.1
    else:
        taxa = 0.15
    return taxa

def calcular_imposto(lista_preços):
    imposto_total = 0
    for preço in lista_preços:
        taxa = definir_taxa(preço)
        imposto = preço * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

print(calcular_imposto(lista_preços))

#OBS: variavel dentro de função so eiste ali dentro,se eu quiser q essa variavel saia da função e so por a varaivel ano return


#Projetinhos com funções

numeros = [1,2]
total = 0
def somar(numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total

print(somar(numeros))

def subtrair(numeros):
    total12 = 0
    for numero in numeros:
        total12 = total12 - numero
    return total12

print(subtrair(numeros))

operação = [5 + 3] 

resultado  = somar(operação)
print(resultado)

nome = input('Digite um nome: ')
def formata_nome(nome):
    nome = nome.capitalize().strip()
    return nome

resultado = formata_nome(nome)
print(resultado)
































