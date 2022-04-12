import re
def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def Tamanho_Médio_Frase(texto):
    lista_sentencas = separa_sentencas(texto)
    soma = 0
    cont = 0
    lista_frase = []
    for i in range(len(lista_sentencas)):
        lista_frase.append(separa_frases(lista_sentencas[i]))
    for j in range(len(lista_frase)):
        for k in range(len(lista_frase[j])):
            soma = soma + (len(lista_frase[j][k]))
            cont += 1
    media = soma/cont
    return (media)

        
