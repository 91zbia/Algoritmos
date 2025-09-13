def anagramas(palavra):
    if len(palavra) == 1:
        return [palavra]
    
    resultado = []
    for i, letra in enumerate (palavra):
        restante = palavra[:i] + palavra[i+1:]
        for anagrama in anagramas(restante):
            resultado.append(letra + anagrama)
    
    return resultado

print(anagramas("bia"))