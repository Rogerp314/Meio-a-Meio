#Arquivo para a função de dividir as strings

def meio(frase):
    if len(frase) % 2 == 0 or len(frase) == 1:
        indicemeio = len(frase) // 2
        palavra_meio = frase[indicemeio]
        return f'A palavra que está no meio da cadeia de strings é {palavra_meio}'
    else:
        palavras = list()
        primeiro_indice = len(frase) // 2 -1
        segundo_indice = len(frase) // 2
        pala1 = frase[primeiro_indice]
        pala2 = frase[segundo_indice]
        palavras.append(pala1)
        palavras.append(pala2)
        palavras_juntas = ' '.join(palavras)
        return f'As palavras que estão no meio da cadeia de strings são {palavras_juntas}'
    
    
if __name__ == '__main__':
    frase = str(input()).split()
    palavra = meio(frase)
    print(palavra)