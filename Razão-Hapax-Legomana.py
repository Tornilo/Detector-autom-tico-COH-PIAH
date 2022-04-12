def Razão_Hapax_Legomana (frase):
    '''Número de palavras utilizadas uma vez dividido
       pelo número total de palavras.'''

    def Frase_Sem_Pontuacao(frase):
    
        Frase_Nova = []
        for i in range(len(frase)):
            if (frase[i] in ("!?,.;:-")) == True:
                A = 0
            else:
                Frase_Nova.append(frase[i])
        frase = "".join(Frase_Nova)
        return (frase)

    def n_palavras_unicas(lista_palavras):
        '''Essa funcao recebe uma lista de palavras e devolve
           o numero de palavras que aparecem uma unica vez'''
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

    frase = Frase_Sem_Pontuacao(frase)
    lista_palavras = frase.split()
    num_tot_pal = len(lista_palavras)
    num_pal_uni = n_palavras_unicas(lista_palavras)

    H_L = num_pal_uni/num_tot_pal
    return (H_L)

