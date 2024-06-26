def notas(*notas, situacao=False):
    """
    Função para analisar as notas e situações das notas dos alunos.
    :param notas: Uma ou mais notas dos alunos. (Aceita várias)
    :param situacao: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Retorna um dicionário com várias informações sobre a situação do aluno.
    """
    analise = dict()
    analise['Total'] = len(notas)
    analise['Maior'] = max(notas)
    analise['Menor'] = min(notas)
    analise['Média'] = sum(notas)/len(notas)
    if situacao:
        if analise['Média'] >= 7:
            analise['Situação'] = 'BOA'
        elif analise['Média'] >= 5:
            analise['Situação'] = 'RAZOÁVEL'
        else:
            analise['Situação'] = 'RUIM'
    return analise

analise = notas(5.5, 2.5, 9, 8,5, situacao=True)
print(analise)