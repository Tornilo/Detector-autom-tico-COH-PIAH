import re
def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def Tamanho_Médio_Sentença (texto):
    lista_sentencas = separa_sentencas(texto)
    soma = 0
    for i in range(len(lista_sentencas)):
        soma = soma + len(lista_sentencas[i])
    cont = len(lista_sentencas)
    media = soma/cont
    return (media)
        
