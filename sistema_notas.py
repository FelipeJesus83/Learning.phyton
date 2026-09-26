alunos = {'João': [7, 8, 9],'Maria': [9, 9, 10],'Pedro': [5, 6, 7]}

def adicionar_nota(alunos):
    aluno = input('Qual seu nome: ').capitalize().strip()
    if aluno in alunos:
        nota = float(input('Qual sua nota: '))
        alunos[aluno].append(nota)
    else:
        print(f'O {aluno}, não existe no sistema')

def calcular_media(alunos):
    aluno = input('Qual seu nome: ').capitalize().strip()
    if aluno in alunos:
        soma = sum(alunos[aluno])
        quantidade = len(alunos[aluno])
        media = soma / quantidade
        print(f'A media do {aluno} é: {media}')
    else:
        print(f'Aluno não está no sistema')
    return media

def listar_alunos(alunos):
    for aluno in alunos:
        print(f'As notas do {aluno} são: {alunos[aluno]}')

def verificacao(alunos):
    aluno = input('Qual seu nome: ').capitalize().strip()
    if aluno in alunos:
        soma = sum(alunos[aluno])
        quantidade = len(alunos[aluno])
        media = soma / quantidade
        if media >= 7:
            print(f'O aluno:{aluno} foi aprovado')
        else:
            print(f'O aluno:{aluno} foi reprovado')
    else:
        print('Aluno não está no sistema')

while True:
    print('=== MENU ===')
    print('1 - Adicionar nota')
    print('2 - Calcular média')
    print('3 - Listar alunos')
    print('4 - Verificar aprovação')
    print('5 - Sair')

    opção = int(input('Digite oque quer fazer: '))
    print(alunos)

    if opção == 1:
        adicionar_nota(alunos)
    elif opção == 2:
        calcular_media(alunos)
    elif opção == 3:
        listar_alunos(alunos)
    elif opção == 4:
        verificacao(alunos)
    elif opção == 5:
        break
    else:
        print('Opção inexistente')
