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

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def Tamanho_Médio_Frase(texto):
    '''é o número total de frases divido pelo número de sentenças.'''
    lista_sentencas = separa_sentencas(texto)
    soma = 0
    for i in range(len(lista_sentencas)):
        Sentencas = (lista_sentencas[i])
        
        
        for j in range(len(separa_frases(lista_sentencas))):
            Frase = separa_frases(lista_sentencas[j])
            print (Frase)

    print(Sentencas)
    print (Frase)
    '''for k in range (len(separa_palavras(Frase))):
                Palavras = 
    cont = len(lista_sentencas)
    media = soma/cont
    return (media)'''
        
