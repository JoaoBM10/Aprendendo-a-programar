print('=='*20)
print(f'{'BANCO CEV':^40}')
print('=='*20)

saque = int(input('Que valor você quer sacar? R$'))
total = saque
cedula = 100
totalcedula = 1

while True:
    while saque % 10 != 0:
        print('Valor inválido')
        print('Saques apenas com cedulas acima de R$10 reais.')
        saque = int(input('Que valor você quer sacar? R$'))
        total = saque
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} cédulas de R${cedula:.2f}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        totalcedula = 0
        if total == 0:
            break
print('=='*20)
print(f'{'BANCO CEV':^40}')
print('=='*20)
