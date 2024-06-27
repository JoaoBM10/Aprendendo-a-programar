from UtilidadesJP import moeda
from UtilidadesJP import dado

preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 20, 5)