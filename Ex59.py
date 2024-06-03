from time import sleep

num1 = float(input('Primeiro valor:'))
num2 = float(input('Segundo valor:'))

sair = False
while not sair:
    menu = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos número
[5] Sair do programa
Qual é sua opção?'''))
    if menu == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é igual a {soma}.')
    elif menu == 2:
        multiplicar = num1 * num2
        print(f'O resultado de {num1} x {num2} é igual a {multiplicar}.')
    elif menu == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é {num1}')
        elif num1 < num2:
            print(f'Entre {num1} e {num2} o maior valor é {num2}')
        else:
            print('Ambos são iguais.')
    elif menu == 4:
        print('Informe os números novamente.')
        num1 = float(input('Primeiro valor:'))
        num2 = float(input('Segundo valor:'))
    elif menu == 5:
        sair = True
    else:
        print('Opção invalida. Tente novamente!')
    print('=-='*10)
print('Finalizando...')
print('=-='*10)
sleep(1)
print('Fim do programa! Volte sempre!')