import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''


    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

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

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
#--------------------------Funçôes Para Calcular a Assinatura----------------------------------
def Frase_Sem_Pontuacao(frase):
    
    Frase_Nova = []
    for i in range(len(frase)):
        if (frase[i] in ("!?,.;:-")) == True:
            A = 0
        else:
            Frase_Nova.append(frase[i])
    frase = "".join(Frase_Nova)
    return (frase)


def Tamanho_médio_palavra (frase):
    '''Média simples do número de caracteres por palavra.'''
    Soma = 0
    cont = 0
    
    Frase = frase.split()
    
    for j in range(len(Frase)):
        Soma = Soma + len(Frase[j])
        cont += 1
    Media = Soma/cont
    return (Media)


def Relação_Type_Token (frase):
    '''Número de palavras diferentes utilizadas em um texto
       divididas pelo total de palavras.'''
    frase = Frase_Sem_Pontuacao(frase)
    lista_palavras = frase.split()
    num_tot_pal = len(lista_palavras)
    num_pal_dif = n_palavras_diferentes(lista_palavras)

    T_T = num_pal_dif/num_tot_pal
    return (T_T)


def Razão_Hapax_Legomana (frase):
    '''Número de palavras utilizadas uma vez dividido
       pelo número total de palavras.'''
    
    frase = Frase_Sem_Pontuacao(frase)
    lista_palavras = frase.split()
    num_tot_pal = len(lista_palavras)
    num_pal_uni = n_palavras_unicas(lista_palavras)

    H_L = num_pal_uni/num_tot_pal
    return (H_L)


def Tamanho_Médio_Sentença (texto):
    '''Média simples do número de caracteres por sentença.'''
    lista_sentencas = separa_sentencas(texto)
    soma = 0
    for i in range(len(lista_sentencas)):
        soma = soma + len(lista_sentencas[i])
    cont = len(lista_sentencas)
    media = soma/cont
    return (media)


def Complexidade_Sentença(texto):
    '''é o número total de frases divido pelo número de sentenças.'''
    lista_sentencas = separa_sentencas(texto)
    soma = 0
    for i in range(len(lista_sentencas)):
        soma = soma + len(separa_frases(lista_sentencas[i]))
    cont = len(lista_sentencas)
    media = soma/cont
    return (media)


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

#----------------------------------------------------------------------------------------------
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    P_b = as_b
    P_a = as_a
    S_a_b = 0
    for i in range(6):
        S_a_b = S_a_b + (P_a[i] - P_b[i])
    Sab = (S_a_b)/6
    return (Sab)
    
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    A = Tamanho_médio_palavra (texto)
    B = Relação_Type_Token (texto)
    C = Razão_Hapax_Legomana (texto)
    D = Tamanho_Médio_Sentença (texto)
    E = Complexidade_Sentença(texto)
    F = Tamanho_Médio_Frase(texto)
    
    return [A, B, C, D, E, F]
    
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto
       com maior probabilidade de ter sido infectado por COH-PIAH.'''
    Lista_Textos = textos
    Modelo_assina = ass_cp
    ind = 1
    for i in range(len(Lista_Textos)):
        T = calcula_assinatura(Lista_Textos[i])
        F = compara_assinatura(Modelo_assina, T)
        temp = F
        ind = i
        if F < temp:
            temp = F
            ind = i
    return (ind)
def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    print()
    ind = (avalia_textos(textos, ass_cp))
    print("O autor do texto", ind,"está infectado com COH-PIAH")
    pass
    
main()

