def Tamanho_médio_palavra (frase):
    '''Média simples do número de caracteres por palavra.'''
    frase = "".join(frase)
    Frase_Nova = []
    Frase = []
    Soma = 0
    cont = 0
    
    for i in range(len(frase)):
        if (frase[i] in (";:,.")) == True:
            Frase.append(" ")
        else:
            Frase.append(frase[i])
    Frase = "".join(Frase)
    
    for j in range(len(Frase)):
        if (Frase[j] in ('";!?,.""[]()"')) == True:
            A = 0
      
        else:
            Frase_Nova.append(Frase[j])
    frase1 = "".join(Frase_Nova)
    print (frase1)
    Frase1 = frase1.split()
    print (Frase1)
    
    for k in range(len(Frase1)):
        Soma = Soma + len(Frase1[k])
        cont += 1
    Media = Soma/cont
    return (Media)
