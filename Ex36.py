valor_casa=float(input('Valor da casa: R$'))
salario=float(input('Salário do comprador: R$'))
financiamento=int(input('Quantos anos de financiamento?'))
prestacao=float(valor_casa/(financiamento*12))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa,financiamento,prestacao))

if prestacao <= salario*0.3:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
