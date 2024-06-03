print('='*10,'LOJA JP','='*10)
valor = float(input('Valor das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] à vista no dinheiro/pix com desconto de 10%
[2] à vista no cartão com desconto de 5%
[3] 2x no cartão
[4] 3x ou mais no cartão com juros de 20%''')

opcao = int(input('Qual é a opção desejada? '))

if opcao == 1:
    total = valor - (valor * 0.1)
elif opcao == 2:
    total = valor - (valor * 0.05)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif opcao == 4:
    total = valor * 1.2
    parcelatotal = int(input('Em quantas parcelas? '))
    parcela = total / parcelatotal
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelatotal , parcela))
else:
    total = valor
    print('Opção inválida! Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor , total))

