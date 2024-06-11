from random import randint

print('=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*10)

contador = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Digite um valor:'))
    opcao = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    condicao = computador + jogador
    print('--'*10)
    if condicao %2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {condicao} DEU PAR')

    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {condicao} DEU ÍMPAR')
    print('--'*10)
    if opcao == 'P' and condicao %2 == 0 or opcao == 'I' and condicao %2 != 0:
        print('Você VENCEU!')
        print('Quero uma REVANCHE!')
        print('=-'*10)
        contador += 1
    else:
        print('HAHAHAHAHAHA!! Você PERDEU!')
        print('--'*10)
        break
print(f'GAME OVER! Você venceu {contador} vezes')    
