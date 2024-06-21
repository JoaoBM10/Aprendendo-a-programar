from datetime import datetime

dados = dict()
dados["Nome"] = str(input('Nome:'))
nasc = int(input('Ano de nascimento:'))
dados["Idade"] = datetime.now().year - nasc
dados["CTPS"] = int(input('Carteira de Trabalho (0 não tem):'))
if dados["CTPS"] != 0:
    dados["Contratação"] = int(input('Ano de contratação:'))
    dados["Salário"] = int(input('Salário: R$'))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"] + 35) - datetime.now().year)
print('='*30)
for keys, values in dados.items():
    print(f'  - {keys}: {values}')