def Relação_Type_Token (frase):
    '''Número de palavras diferentes utilizadas em um texto
       divididas pelo total de palavras.'''

    def Frase_Sem_Pontuacao(frase):
    
        Frase_Nova = []
        for i in range(len(frase)):
            if (frase[i] in ("!?,.;:-")) == True:
                A = 0
            else:
                Frase_Nova.append(frase[i])
        frase = "".join(Frase_Nova)
        return (frase)

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

    frase = Frase_Sem_Pontuacao(frase)
    lista_palavras = frase.split()
    num_tot_pal = len(lista_palavras)
    num_pal_dif = n_palavras_diferentes(lista_palavras)

    T_T = num_pal_dif/num_tot_pal
    return (T_T)

