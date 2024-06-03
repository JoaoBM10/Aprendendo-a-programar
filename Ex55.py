maior = 0
menor = 0
for intervalo in range(1 , 6 , 1):
    peso = float(input(f'Digite o peso da {intervalo}ª pessoa:'))
    if intervalo == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é de {maior}Kg.')
print(f'O menor peso é de {menor}Kg.')
