tarefas = []

tarefa1 = input('Qual primeira tarefa você quer fazer? ')
tarefas.append(tarefa1)
print(tarefa1.capitalize().strip())

tarefa2 = input('Qual segunda tarefa você quer fazer? ')
tarefas.append(tarefa2)
print(tarefa2.capitalize().strip())

tarefa3 = input('Qual terceira tarefa você quer fazer? ')
tarefas.append(tarefa3)
print(tarefa3.capitalize().strip())

quantidade = len(tarefas)
print(f'A quantidade de tarefas é: {quantidade}')

posição = tarefas.index(tarefa1)
print(f'A posição da tarefa 1 é: {posição}')

print('Remoção da tarefa 3')
tarefas.remove(tarefa3)
print(tarefas)








































































