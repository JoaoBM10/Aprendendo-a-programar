valores = list()

for contador in range(0,5):
    valores.append(int(input('Digite um valor:')))
print(valores)

print(f'O maior valor da lista é {max(valores)} e está na posição', end=' ')
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{posicao}...', end= ' ')
print()
print(f'O menor valor da lista é {min(valores)} e está na posição', end=' ')
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{posicao}...', end=' ')
print()